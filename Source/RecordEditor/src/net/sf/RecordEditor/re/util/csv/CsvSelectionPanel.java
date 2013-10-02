package net.sf.RecordEditor.re.util.csv;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.List;
import java.util.StringTokenizer;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.text.JTextComponent;

import net.sf.JRecord.ByteIO.ByteTextReader;
import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.Conversion;
import net.sf.JRecord.CsvParser.ParserManager;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.Types.Type;
import net.sf.RecordEditor.utils.MenuPopupListener;
import net.sf.RecordEditor.utils.edit.ManagerRowList;
import net.sf.RecordEditor.utils.lang.ReAbstractAction;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.BmKeyedComboBox;
import net.sf.RecordEditor.utils.swing.BmKeyedComboModel;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.ComboBoxs.DelimiterCombo;
import net.sf.RecordEditor.utils.swing.ComboBoxs.QuoteCombo;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeCombo;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeComboItem;

@SuppressWarnings("serial")
public class CsvSelectionPanel extends BaseHelpPanel implements FilePreview {

	public static final String NORMAL_CSV_STRING  = "CSV";
	public static final String UNICODE_CSV_STRING = "UNICODECSV";

	//private static final int FILE_HEIGHT = SwingUtils.TABLE_ROW_HEIGHT * 27 / 2;


	private boolean isByteBased = true;

	private ParserManager parserManager = ParserManager.getInstance();
	private MenuPopupListener popup;
	private String	lastFont = null,
					lastSeperator = null;
//	private String[] lines = null;
//	private int lines2display = 0;


	private BmKeyedComboModel styleModel = new BmKeyedComboModel(
												new ManagerRowList(parserManager, false));
    public final DelimiterCombo fieldSeparator;
    public final JTextField fieldSepTxt = new JTextField(5);
    public final JTextField quoteTxt = new JTextField(5);
    public final QuoteCombo quoteCombo = QuoteCombo.newCombo();
    //public JTextField fontTxt = new JTextField();
    private final TreeCombo charsetCombo = new TreeCombo(null);

    public BmKeyedComboBox parseType  = new BmKeyedComboBox(styleModel, false);

    public JCheckBox fieldNamesOnLine = new JCheckBox();
    public JTextField nameLineNoTxt = new JTextField();
    public JCheckBox checkTypes = new JCheckBox();
    public JCheckBox embeddedCrJCheck = new JCheckBox();

    public JButton go = SwingUtils.newButton("Go");
    public JButton cancel = SwingUtils.newButton("Cancel");

    private JTable linesTbl = new JTable();

    private AbstractCsvTblMdl tblMdl;
    private JTextComponent message;

    private boolean doAction = true;
    private byte[][] dataLines = null;
    private byte[] data;

    private ActionListener changedAction = new ActionListener() {
    	   public void actionPerformed(ActionEvent e) {

    		   if (doAction) {
    			   valueChanged();
    		   }
    	   }
    };
    private ChangeListener changeListner = new ChangeListener() {

		/* (non-Javadoc)
		 * @see javax.swing.event.ChangeListener#stateChanged(javax.swing.event.ChangeEvent)
		 */
		@Override
		public void stateChanged(ChangeEvent e) {
 			if (doAction) {
 				if ((lastFont == null || ! lastFont.equals(charsetCombo.getText()))) {
 					setData("", data, false, "");
					valueChanged(false);
 				}
		   }
		}
    };

    private ActionListener fieldNamesChanged = new ActionListener() {
   	   public void actionPerformed(ActionEvent e) {

	   		if (doAction) {
	   		   tblMdl.setSeperator(getSeperator());
	   		   tblMdl.setHideFirstLine(fieldNamesOnLine.isSelected());

	   		   valueChanged();
	   		}
   	   }
    };

    private ActionListener sepChanged  = new ActionListener() {
    	public void actionPerformed(ActionEvent e) {
	 		if (doAction) {
	 			String seperator = getSeperator();
	 			if ((! seperator.equals(lastSeperator))
	 			||	embeddedCrJCheck.isSelected()) {
	 				lastSeperator = seperator;
	 				reReadData();
	 			}
 				valueChanged(false);
	 		}
    	}
     };

     private ActionListener crChanged = new ActionListener() {
     	public void actionPerformed(ActionEvent e) {

 	 		if (doAction) {
	 	 		if (embeddedCrJCheck.isSelected() && "".equals(getQuote())) {
	 	 			try {
	 	 				doAction = false;

	 	 				tblMdl.setEmbedded(true);
	 	 				CsvAnalyser anaylyser = tblMdl.getAnalyser(AbstractCsvTblMdl.DERIVE_SEPERATOR);

	 	 				if (anaylyser.getQuoteIdx() > 0) {
	 	 					quoteCombo.setSelectedIndex(anaylyser.getQuoteIdx());
	 	 				}
 	 				} finally {
 	 					doAction = true;
 	 				}
	 	 		}
	 		   reReadData();
 	 		   valueChanged(false);
 	 		}
 	 		if (embeddedCrJCheck.isSelected() && "".equals(getQuote())) {
	 			CsvSelectionPanel.this.setMessageTxt("You must specify a quote when embedded Cr is used");
 	 		}
      	}
      };

    private FocusAdapter focusHandler = new FocusAdapter() {
    	public void focusLost(FocusEvent e) {

    		boolean reRead = true;
    		String seperator = getSeperator();
			if ((e.getSource() == charsetCombo.getTextCompenent()
			&& (lastFont == null || ! lastFont.equals(charsetCombo.getText()))) ) {
    			lastFont = charsetCombo.getText();
    			if (dataLines == null) {
    				setData("", data, false, "");
    				reRead = false;
    			} else {
    				setData(dataLines, lastFont);
    			}
			} else if (e.getSource() == embeddedCrJCheck
		    		|| (   (e.getSource() == fieldSeparator || e.getSource() == fieldSepTxt)
		        		&& (! seperator.equals(lastSeperator) )	)) {
    			lastSeperator = seperator;
    			if (dataLines == null) {
    				reReadData();
    				reRead = false;
    			} else {
    				setData(dataLines, lastFont);
    			}
    		} else if (embeddedCrJCheck.isSelected() && dataLines == null) {
    			reReadData();
    			reRead = false;
    		}
    		valueChanged(reRead);
    	}
    };


	public CsvSelectionPanel(byte[][] dataLines, String font,
			boolean showCancel, JTextComponent msg) {
		this(dataLines, font, showCancel, "", msg, false);
    };


	public CsvSelectionPanel(byte[][] dataLines, String font,
			boolean showCancel, String heading, JTextComponent msg,
			boolean adjustableTblHeight) {
		fieldSeparator = DelimiterCombo.NewDelimCombo();
		message = msg;
		setData(dataLines, font);

		init_100_SetupFields();
		init_200_LayoutScreen(showCancel, heading, adjustableTblHeight);
	};


	public CsvSelectionPanel(byte[] data, String font,
			boolean showCancel, String heading, JTextComponent msg,
			boolean adjustableTblHeight) {
		message = msg;
		isByteBased = false;
		fieldSeparator = DelimiterCombo.NewDelimCombo();

		setData("", data, true, null);

		init_100_SetupFields();
		init_200_LayoutScreen(showCancel, heading, adjustableTblHeight);
		valueChanged(false);
	};

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getContainer()
	 */
	@Override
	public BaseHelpPanel getPanel() {
		return this;
	}


	@Override
	public JButton getGoButton() {
		return go;
	}


	@Override
	public String getFontName() {
		return charsetCombo.getText();
	}


	private void setData(byte[][] dataLines, String font) {
		CsvAnalyser anaylyser = new CsvAnalyser(dataLines, -1, "", embeddedCrJCheck.isSelected());
		setUpSeperator(anaylyser);

		this.dataLines = dataLines;

		tblMdl = new CsvSelectionTblMdl(parserManager);
		tblMdl.setLines(dataLines, font);
		tblMdl.setFieldLineNo(getFieldLineNo());

		linesTbl.setModel(tblMdl);
		valueChanged(true);
	}



	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#setData(byte[], boolean)
	 */
	@Override
	public boolean setData(String filename, byte[] data, boolean checkCharset, String layoutId) {
		if (layoutId != null && ! "".equals(layoutId)) {
			setFileDescription(layoutId);
		}

		String font = charsetCombo.getText();
		CsvAnalyser anaylyser;
		boolean reRead = false;


		this.data = data;
		if (data == null || data.length == 0) {
			return false;
		}
		dataLines = null;
		this.lastFont = font;

		CharsetDetails charsetDetails = CheckEncoding.determineCharSet(data, true);
		if (checkCharset) {
			font = charsetDetails.charset;
			setCharset(font);
		}
		setCharsetCombo(charsetDetails);


		setTblMdl(isBinarySep() || possibleBinarySep(data, font), font);

		//anaylyser = new CsvAnalyser(tblMdl.getLinesString(), -1, font);
		anaylyser = tblMdl.getAnalyser(AbstractCsvTblMdl.DERIVE_SEPERATOR);

		reRead = embeddedCrJCheck.isSelected() && anaylyser.getQuoteIdx() > 0 && "".equals(getQuote());
		setUpSeperator(anaylyser);

		tblMdl.setFieldLineNo(getFieldLineNo());

		linesTbl.setModel(tblMdl);
		valueChanged(reRead);

		return anaylyser.isValidChars();
	}

	public final void setCharset(String charset) {

		try {
			charsetCombo.setText(charset);
		} finally {
			doAction = false;
		}
	}

	private void setCharsetCombo(CharsetDetails dtls) {

		TreeComboItem[] items;
		String currCharset = charsetCombo.getText();
		TreeComboItem currCharsetItm = new TreeComboItem(1, currCharset, currCharset);
		if (dtls.likelyCharsets == null || dtls.likelyCharsets.length == 0) {
			items = new TreeComboItem[] {currCharsetItm};
		} else {
			int noCharSets = dtls.likelyCharsets.length + 1;
			int j = 0;

			for (String c : dtls.likelyCharsets) {
				if (currCharset.equalsIgnoreCase(c)) {
					noCharSets -= 1;
					break;
				}
			}

			items = new TreeComboItem[Math.min(10, noCharSets)];
			items[j++] = currCharsetItm;
			for (int i = 0; j < items.length && i < dtls.likelyCharsets.length; i++) {
				if (! currCharset.equalsIgnoreCase(dtls.likelyCharsets[i])) {
					items[j++] = new TreeComboItem(i, dtls.likelyCharsets[i], dtls.likelyCharsets[i]);
				}
			}

		}
		charsetCombo.setTree(items);
	}

	private boolean possibleBinarySep(byte[] data, String font)  {
		boolean ret = false;

		if (Conversion.isSingleByte(font)) {
			try {
				List<byte[]> l = ByteTextReader.readStream(font, new ByteArrayInputStream(data), 90);
				byte[][] lines = l.toArray(new byte[l.size()][]);
				String sep = CsvAnalyser.getSeperator(lines, lines.length, font);

				ret = sep != null && sep.startsWith("x'");
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		return ret;
	}

	private void reReadData() {

		if (data == null || (dataLines != null)) {
			return;
		}

		setTblMdl(isBinarySep(), charsetCombo.getText());

		tblMdl.setFieldLineNo(getFieldLineNo());
		linesTbl.setModel(tblMdl);
	}

	private void setTblMdl(boolean useByteMdl, String font) {

		if (useByteMdl) {
			tblMdl = new CsvSelectionTblMdl(parserManager);
		} else {
			tblMdl = new CsvSelectionStringTblMdl(parserManager);
		}

		tblMdl.setParserType(((Integer) parseType.getSelectedItem()).intValue());
		tblMdl.setQuote(getQuote());
		tblMdl.setSeperator(getSeperator());
		tblMdl.setDataFont(data, font,
				embeddedCrJCheck.isSelected());
	}

	/**
	 * Setup screen fields
	 *
	 */
	private void init_100_SetupFields() {

		nameLineNoTxt.setText("1");
		fieldSeparator.addFocusListener(focusHandler);
		fieldSepTxt.addFocusListener(focusHandler);
		quoteCombo.addFocusListener(focusHandler);
		quoteTxt.addFocusListener(focusHandler);
		parseType.addFocusListener(focusHandler);
		charsetCombo.getTextCompenent().addFocusListener(focusHandler);
		fieldNamesOnLine.addFocusListener(focusHandler);
		nameLineNoTxt.addFocusListener(focusHandler);
		embeddedCrJCheck.addFocusListener(focusHandler);

		fieldSeparator.addActionListener(sepChanged);
		quoteCombo.addActionListener(changedAction);
		quoteTxt.addActionListener(changedAction);
		parseType.addActionListener(changedAction);
		charsetCombo.addFileChangeListner(changeListner);
		fieldNamesOnLine.addActionListener(fieldNamesChanged);
		embeddedCrJCheck.addActionListener(crChanged);
	}

	private void init_200_LayoutScreen(boolean showCancel, String heading, boolean adjustableTblHeight) {
		double fileTblHeight = SwingUtils.TABLE_ROW_HEIGHT * 27 / 2;
		JPanel fieldSeperatorPnl = init_200_bld2fieldPnl(fieldSeparator, fieldSepTxt, "FieldSep");
		JPanel quotePnl = init_200_bld2fieldPnl(quoteCombo, quoteTxt, "Quote");
		//pnl1.add(BorderLayout.WEST, pnl);

		if (heading != null && ! "".equals(heading)) {
			JLabel headingLabel = new JLabel("  " + heading + "  ");
			Font font = headingLabel.getFont();
			headingLabel.setBackground(Color.WHITE);
			headingLabel.setOpaque(true);
			headingLabel.setFont(new Font(font.getFamily(), Font.BOLD, font.getSize() +2));

			this.addHeadingComponent(headingLabel);
			this.setGap(GAP0);
		}
		addLine("Field Seperator", fieldSeperatorPnl);
		setGap(GAP1);

		addLine("Quote", quotePnl);

		if (! isByteBased) {
			addLine("Font", charsetCombo);
		}
		if (adjustableTblHeight) {
			fileTblHeight = BasePanel.FILL;
		} else if (! isByteBased) {
			fileTblHeight -= SwingUtils.TABLE_ROW_HEIGHT * 2;
		}
		addLine("Parser", parseType);
		addLine("Names on Line", fieldNamesOnLine);

		if (showCancel) {
			addLine("Line Number of Names", nameLineNoTxt, go);
			setGap(BasePanel.GAP);
			addLine("set Column Types", checkTypes);
			addLine("embedded New Lines", embeddedCrJCheck, cancel);
			setGap(BasePanel.GAP);
		} else {
			addLine("Line Number of Names", nameLineNoTxt);
			addLine("set Column Types", checkTypes);
			addLine("embedded New Lines", embeddedCrJCheck, go);
			setGap(BasePanel.GAP1);
		}

		this.addComponent(
				1, 5, fileTblHeight, BasePanel.GAP,
		        BasePanel.FULL, BasePanel.FULL,
		        new JScrollPane(linesTbl));

		if (message == null) {
			message = new JTextField();

			this.setGap(GAP1);
			this.addMessage(message);
			this.setHeight(HEIGHT_1P4);
		} else {
			super.setMessage(message);
		}

		popup = new MenuPopupListener();
		popup.setTable(linesTbl);
		popup.getPopup().add(new ReAbstractAction("set as Field Name Row") {
			public void actionPerformed(ActionEvent e) {
				int inc = 1;
				if (fieldNamesOnLine.isSelected() && getFieldLineNo() == 1) {
					inc = 2;
				}
//				System.out.println("Set Row " + fieldNamesOnLine.isSelected()
//						+ " " + getFieldLineNo()
//						+ " " + inc
//						+ " " + popup.getPopupRow());
				fieldNamesOnLine.setSelected(true);
				nameLineNoTxt.setText(Integer.toString(popup.getPopupRow() + inc));
				valueChanged();
			}
		});
		linesTbl.addMouseListener(popup);
	}


	private JPanel init_200_bld2fieldPnl(JComponent field1, JComponent field2, String fieldName) {
		JPanel ret = new JPanel(new BorderLayout());

		JPanel pnl1 = new JPanel();
		JLabel orLbl = new JLabel("   or ");
		linesTbl.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);

		pnl1.add(orLbl);
		//pnl1.add(fieldSepTxt);
		orLbl.setAlignmentX(JLabel.CENTER_ALIGNMENT);
		//pnl.setLayout();
		ret.add(BorderLayout.WEST, field1);
		ret.add(BorderLayout.CENTER, pnl1);
	   //pnl.add(BorderLayout.CENTER, orLbl);
		ret.add(BorderLayout.EAST, field2);
		ret.setMinimumSize(new Dimension(ret.getPreferredSize().width, SwingUtils.TABLE_ROW_HEIGHT));

		setComponentName(field2, fieldName);

		return ret;
	}


	private void valueChanged() {
		valueChanged(true);
	}


	private void valueChanged(boolean reRead) {


		try {
			doAction = false;
			String quoteStr = getQuote();

			if (reRead && embeddedCrJCheck.isSelected() || tblMdl == null) {
				reReadData();
			} else {
				tblMdl.setParserType(((Integer) parseType.getSelectedItem()).intValue());
				tblMdl.setQuote(quoteStr);
				tblMdl.setSeperator(getSeperator());
				tblMdl.setFont(charsetCombo.getText());
			}

			if (tblMdl != null) {
				if (tblMdl.getRowCount() > 0) {
					try {
						String l = tblMdl.getLine(0).trim();

						tblMdl.setFieldLineNo(getFieldLineNo());
						if (fieldNamesOnLine.isSelected() && ! "".equals(quoteStr)
						&& l.startsWith(quoteStr) && l.endsWith(quoteStr)
						&& parseType.getSelectedIndex() == 0) {
							parseType.setSelectedIndex(3);
							tblMdl.setParserType(((Integer) parseType.getSelectedItem()).intValue());
						}

				 		tblMdl.setHideFirstLine(fieldNamesOnLine.isSelected());
					} catch (Exception e) {
					}
				}
				tblMdl.setupColumnCount();
				tblMdl.fireTableStructureChanged();
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			doAction = true;
		}
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getSeperator()
	 */
	@Override
	public final String getSeperator() {

		String sep = fieldSepTxt.getText();

		if (sep == null || "".equals(sep) || ! isSepValid()) {
			sep = fieldSeparator.getSelectedEnglish();
		}

		if ("<Space>".equals(sep)) {
			sep = " ";
		} else if ("<Tab>".equals(sep)) {
			sep = "\t";
		} else if ("<Default>".equals(sep)) {
			sep = ",";
		}

		return sep;
	}

	/**
	 * Check if field seperator is valid
	 * @return wether the field seperator is valid
	 */
	private boolean isSepValid() {
		boolean ret = false;
		String v = fieldSepTxt.getText();
		boolean singleByte = Conversion.isSingleByte(charsetCombo.getText());

		if (v.length() < 2) {
			ret = true;
		} else if (singleByte && isValidTextBinarySep()) {
			try {
				Conversion.getByteFromHexString(v);
				ret = true;
			} catch (Exception e) {
				setMessageTxt("Invalid Delimiter - Invalid  hex string:", v.substring(2, 3));
			}
		} else if (singleByte) {
			setMessageTxt("Invalid Delimiter, should be a single character or a hex character");
		} else {
			setMessageTxt("Invalid Delimiter, should be a single character");
		}

		return ret;
	}

	private boolean isValidTextBinarySep() {
		String v = fieldSepTxt.getText();
		return ((v.length() == 5) && v.toLowerCase().startsWith("x'") && v.endsWith("'"));
	}


	private boolean isBinarySep() {
		String v = getSeperator();
		return (v.toLowerCase().startsWith("x'") && v.endsWith("'"));
	}

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getQuote()
	 */
	@Override
	public final String getQuote() {
		String q = quoteTxt.getText();
		if (q == null || "".equals(q)) {
			return quoteCombo.getSelectedKey();
		}
		return q;
	}



	/**
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#setLines(byte[][], java.lang.String, int)
	 */
	@Override
	public boolean setLines(byte[][] newLines, String font, int numberOfLines) {
		CsvAnalyser analyser = new CsvAnalyser(newLines, numberOfLines, "", embeddedCrJCheck.isSelected());
		tblMdl.setLines(newLines, font);
		tblMdl.setLines2display(numberOfLines);

		setUpSeperator(analyser);
		tblMdl.setFieldLineNo(getFieldLineNo());
		valueChanged();

		return analyser.isValidChars();
	}




	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#setLines(java.lang.String[], java.lang.String, int)
	 */
	@Override
	public void setLines(String[] newLines, String font, int numberOfLines) {

		tblMdl.setLines(newLines);
		tblMdl.setLines2display(numberOfLines);
		setUpSeperator(new CsvAnalyser(newLines, numberOfLines, "", embeddedCrJCheck.isSelected()));
		valueChanged();
	}

	private void setUpSeperator(CsvAnalyser analyse) {

		try {
			this.doAction = false;
			fieldSeparator.setSelectedIndex(analyse.getSeperatorIdx());
			fieldSepTxt.setText("");
			quoteCombo.setSelectedIndex(analyse.getQuoteIdx());

			switch (analyse.getColNamesOnFirstLine()) {
			case CsvAnalyser.COLUMN_NAMES_NO:
				fieldNamesOnLine.setSelected(false);
				nameLineNoTxt.setText("1");
				break;
			case CsvAnalyser.COLUMN_NAMES_YES:
				fieldNamesOnLine.setSelected(true);
				nameLineNoTxt.setText(Integer.toString(analyse.getFieldNameLineNo()));
				break;
			}
		} finally {
			this.doAction = true;
		}
	}

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getColumnCount()
	 */
	@Override
	public int getColumnCount() {
		return tblMdl.getColumnCount();
	}



	@Override
	public String getColumnName(int idx) {
		return tblMdl.getColumnName(idx);
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getLayout(java.lang.String, byte[])
	 */
	@Override
	public LayoutDetail getLayout(String font, byte[] recordSep) {
		LayoutDetail layout;

	    int numCols = getColumnCount();
	    int ioId = Constants.IO_BIN_TEXT;
        int format    = 0;
        int i         = 0;
        int fldLineNo = getFieldLineNo();
        String param  = "";
	    String s;

	    int fieldType ;
	    int[] fieldTypes = null;

        RecordDetail.FieldDetails[] flds = new RecordDetail.FieldDetails[numCols];
        RecordDetail[] recs = new RecordDetail[1];

        if (Conversion.isSingleByte(font)) {
        	if (fieldNamesOnLine.isSelected() && fldLineNo < 2) {
        		ioId = Constants.IO_BIN_NAME_1ST_LINE;
        	}
        } else {
        	ioId = Constants.IO_UNICODE_TEXT;
        	if (fieldNamesOnLine.isSelected() && fldLineNo < 2) {
        		ioId = Constants.IO_UNICODE_NAME_1ST_LINE;
        	}
        }

        CsvAnalyser analyser = tblMdl.getAnalyser(AbstractCsvTblMdl.USE_CURRENT_SEPERATOR);
		if (checkTypes.isSelected()
        || parseType.getSelectedIndex() == 2
        || parseType.getSelectedIndex() == 5) {
         	fieldTypes = analyser.getTypes();
        } else {
         	fieldTypes = analyser.getTextTypes();
       }

	    for (i = 0; i < numCols; i++) {
	    	fieldType = Type.ftChar;
	    	if (fieldTypes != null && i < fieldTypes.length) {
	    		fieldType = fieldTypes[i];
	    	}
		    s = getColumnName(i);

            flds[i] = new RecordDetail.FieldDetails(s, s, fieldType, 0,
                        font, format, param);
            flds[i].setPosOnly(i + 1);
	    }

        recs[0] = new RecordDetail("GeneratedCsvRecord", "", "", Constants.rtDelimited,
        		getSeperator(),  getQuote(), font, flds,
        		((Integer)parseType.getSelectedItem()).intValue(), 0, embeddedCrJCheck.isSelected());

        layout  =
            new LayoutDetail("GeneratedCsv", recs, "",
                Constants.rtDelimited,
                recordSep, "", font, null,
                ioId
            );

        layout.setUseThisLayout(true);
		return layout;
	}

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#getFileDescription()
	 */
	@Override
	public String getFileDescription() {
		String csv = UNICODE_CSV_STRING;

		if (isByteBased) {
			csv = NORMAL_CSV_STRING;
		}


		return csv	+ SEP + fieldSeparator.getSelectedIndex()
					+ SEP + getStr(fieldSepTxt.getText())
					+ SEP + quoteCombo.getSelectedEnglish()
					+ SEP + parseType.getSelectedIndex()
					+ SEP + getBool(fieldNamesOnLine)
					+ SEP + getBool(checkTypes)
					+ SEP + getStr(charsetCombo.getText())
					+ SEP + getStr(nameLineNoTxt.getText())
					+ SEP + getStr(quoteTxt.getText())
					+ SEP + getBool(embeddedCrJCheck)

					;
	}

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.csv.FilePreview#setFileDescription(java.lang.String)
	 */
	@Override
	public void setFileDescription(String val) {
		StringTokenizer tok = new StringTokenizer(val, SEP, false);

		try {
			doAction = false;
			System.out.print(tok.nextToken());
			fieldSeparator.setSelectedIndex(getIntTok(tok));
			fieldSepTxt.setText(getStringTok(tok));
			quoteCombo.setEnglish(getStringTok(tok));
			parseType.setSelectedIndex(getIntTok(tok));
			fieldNamesOnLine.setSelected(getBoolTok(tok));
			checkTypes.setSelected(getBoolTok(tok));
			charsetCombo.setText(getStringTok(tok));
			nameLineNoTxt.setText(getStringTok(tok));
			quoteTxt.setText(getStringTok(tok));
			embeddedCrJCheck.setSelected(getBoolTok(tok));
		} catch (Exception e) {

		} finally {
			doAction = true;
		}
	}

	private String getBool(JCheckBox chk) {
		String s = "N";
		if (chk.isSelected()) {
			s = "Y";
		}
		return s;
	}

	private String getStr(String s) {
		if (s == null || "".equals(s)) {
			s = NULL_STR;
		}

		return s;
	}

	private int getIntTok(StringTokenizer tok) {
		int ret = 0;
		try {
			ret = Integer.parseInt(tok.nextToken());
		} catch (Exception e) {
			// TODO: handle exception
		}

		return ret;
	}


	private boolean getBoolTok(StringTokenizer tok) {

		return "Y".equalsIgnoreCase(tok.nextToken());
	}



	private String getStringTok(StringTokenizer tok) {

		String s = tok.nextToken();
		if (s == null || NULL_STR.equals(s)) {
			s = "";
		}
		return s;
	}

	private int getFieldLineNo() {
		int ret = 1;
		String s = nameLineNoTxt.getText();
		if (! "".equals(s)) {
			try {
				ret = Integer.parseInt(s);

				if (ret < 1) {
					ret = 1;
					setMessageTxt("Field Line Number should be one or more and not",  s);
				}
			} catch (Exception e) {
				setMessageTxt("Invalid Field Line Number:", s);
			}
		}


		return ret;
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.re.util.csv.FilePreview#isMyLayout(java.lang.String)
	 */
	@Override
	public boolean isMyLayout(String layout) {
		return false;
	}
}
