package net.sf.RecordEditor.edit.display.SaveAs;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import javax.management.RuntimeErrorException;
import javax.swing.ButtonGroup;
import javax.swing.DefaultCellEditor;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.TableColumnModel;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.JRecord.Details.AbstractLine;
import net.sf.JRecord.Details.AbstractRecordDetail;
import net.sf.RecordEditor.edit.open.StartEditor;
import net.sf.RecordEditor.edit.util.StandardLayouts;
import net.sf.RecordEditor.re.file.AbstractLineNode;
import net.sf.RecordEditor.re.file.DisplayType;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.re.fileWriter.FieldWriter;
import net.sf.RecordEditor.re.script.ScriptData;
import net.sf.RecordEditor.re.util.ReIOProvider;
import net.sf.RecordEditor.utils.charsets.FontCombo;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.CheckBoxTableRender;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.ComboBoxs.DelimiterCombo;
import net.sf.RecordEditor.utils.swing.ComboBoxs.QuoteCombo;
import net.sf.RecordEditor.utils.swing.treeCombo.FileSelectCombo;

public abstract class SaveAsPnlBase {

	public final static int SINGLE_TABLE = 1;
	public final static int TABLE_PER_ROW = 2;
	public final static int TREE_TABLE = 3;
	public final static String[] FIXED_COL_NAMES = LangConversion.convertColHeading(
			"Export_Field_Selection",
			new String[] {"Field Name", "Include", "Length"});

	public final static String[] TITLES = LangConversion.convertArray(LangConversion.ST_TAB, "ExportTab", new String[] {
		"Data",
		"CSV",
		"Fixed",
		"Xml",
		"Html",
		"Script",
		"XSLT Transform",
		"Velocity",
		"File Structure"
	});

//	public final static String[] XSLT_OPTIONS = {
//		"",
//		"net.sf.saxon.TransformerFactoryImpl",
//		"org.apache.xalan.processor.TransformerFactoryImpl"
//	};


	private final static int NULL_INT = Constants.NULL_INTEGER;
	private final static int COL_NAME = 0;
	private final static int COL_INCLUDE = 1;
	private final static int COL_LENGTH = 2;

	private final static int[] FMT_TO_NUMBER_OF_COLS = {1, 2, 3};


	private final String extension;
	public final int panelFormat, extensionType;

	protected final CommonSaveAsFields commonSaveAsFields;


	public final BaseHelpPanel panel = new BaseHelpPanel(this.getClass().getSimpleName());

    public final DelimiterCombo delimiterCombo  = DelimiterCombo.NewDelimCombo();
    public final QuoteCombo quoteCombo = QuoteCombo.newCombo();
    public final JCheckBox quoteAllTextFields = new JCheckBox();
//    public final JTextField charsetTxt  = new JTextField();
    public final JTextField xsltTxt  = new JTextField();

//    public final JTextField charsetTxt = new JTextField();
    public final FontCombo charsetCombo = new FontCombo(); 

    private   final ButtonGroup tableTypeGrp = new ButtonGroup();
    protected final JRadioButton singleTable = genTableTypeBtn("Single Table");
    protected final JRadioButton tablePerRow = genTableTypeBtn("Table per Row");
    protected final JRadioButton treeTable   = genTableTypeBtn("Tree Table");

    public final JCheckBox onlyData   = new JCheckBox();
    public final JCheckBox showBorder = new JCheckBox();
    public final JCheckBox namesFirstLine = new JCheckBox();
    public final JCheckBox spaceBetweenFields = new JCheckBox();
    public final FileSelectCombo template;

	protected final JButton selectBtn;
	protected final JButton deSelectBtn;

    protected final JTable fieldTbl;
    protected FldTblMdl fieldModel;


    private AbstractRecordDetail record;
    private int[] fieldLengths, suppliedFieldLengths;
    private boolean[] includeFields;


    public int rowCount;

    private FileView file;



    public SaveAsPnlBase(CommonSaveAsFields commonSaveAsFields, String extension, int panelFormat, int extensionType,
    		FileSelectCombo template, boolean useFieldTbl ) {
		super();

		this.commonSaveAsFields = commonSaveAsFields;
		this.extension = extension;
		this.panelFormat = panelFormat;
		this.extensionType = extensionType;
		this.template = template;
		this.delimiterCombo.setSelectedIndex(0);
		this.quoteCombo.setTextValue("\"");
		
		file = commonSaveAsFields.getRecordFrame().getFileView();

        String f = file.getLayout().getFontName();
		if (f != null && f.toLowerCase().startsWith("utf")) {
   			charsetCombo.setText(f);
   		}
		
		if (useFieldTbl) {
			fieldTbl = new JTable();
			selectBtn = SwingUtils.newButton("Select All Fields");
			deSelectBtn = SwingUtils.newButton("Deselect All Fields");
			
			selectBtn.addActionListener(new SelectAction(true));
			deSelectBtn.addActionListener(new SelectAction(false));
		} else {
			fieldTbl = null;
			selectBtn = null;
			deSelectBtn = null;
		}
	}

    protected final JPanel getSelectBtnPnl() {
    	JPanel btnPnl = new JPanel();
		
    	btnPnl.add(selectBtn);
		btnPnl.add(deSelectBtn);
		
		return btnPnl;
    }

    protected final void addDescription(String s) {
		JTextArea area = new JTextArea(s);

		panel.addComponentRE(1, 5,BasePanel.FILL, BasePanel.GAP,
                BasePanel.FULL, BasePanel.FULL,
                area);
	}

    protected final void addHtmlFields(BasePanel pnl) {
    	pnl.addLineRE("Only Data Column", onlyData);
    	pnl.addLineRE("Show Table Border", showBorder);
    }


	private JRadioButton genTableTypeBtn(String s) {
    	return generateRadioButton(tableTypeGrp, s);
    }


	protected final JRadioButton generateRadioButton(ButtonGroup grp, String s) {
    	JRadioButton btn = new JRadioButton(LangConversion.convert(LangConversion.ST_FIELD,s));

    	grp.add(btn);
    	return btn;
    }

   public int getTableOption() {
    	int ret = SINGLE_TABLE;

    	if (this.tablePerRow.isSelected()) {
    		ret = TABLE_PER_ROW;
    	} else if (this.treeTable.isSelected()) {
    		ret = TREE_TABLE;
    	}

    	return ret;
    }

    public void setTableOption(int opt) {
    	switch (opt) {
    	case SINGLE_TABLE:  this.singleTable.setSelected(true); break;
    	case TABLE_PER_ROW: this.tablePerRow.setSelected(true); break;
    	case TREE_TABLE:    this.treeTable.setSelected(true);   break;
    	}
    }

	public String getTitle() {
		return TITLES[this.panelFormat];
	}

	public String getQuote() {
//		String ret = "";
//		int idx = quoteCombo.getSelectedIndex();
//
//		if (idx >= 0) {
//			ret = Common.QUOTE_VALUES[idx];
//		}

		return quoteCombo.getQuote();
	}

	public String getCharset() throws RecordException {
		String charset = charsetCombo.getText();
		
		if (!("".equals(charset) || Charset.isSupported(charset))) {
			throw new RecordException("Charset is not supported by this Java implementation");
		}
		
		return charset;
	}

	/**
	 * @return the extension
	 */
	public String getExtension() {
		return extension;
	}


	/**
	 * @return the fieldLengths
	 */
	public int[] getFieldLengths() {

		if (this.namesFirstLine.isSelected() && record != null) {
			for (int i = 0; i < fieldLengths.length; i++) {
				if (fieldLengths[i] < 0) {
					fieldLengths[i] = Math.max(
							suppliedFieldLengths[i],
							record.getField(i).getName().length());
				}
			}
		} else {
			for (int i = 0; i < fieldLengths.length; i++) {
				if (fieldLengths[i] < 0) {
					fieldLengths[i] = suppliedFieldLengths[i];
				}
			}
		}

		return fieldLengths;
	}

	/**
	 * @return the includeFields
	 */
	public boolean[] getIncludeFields() {
		return includeFields;
	}

	private void setIncludeFields(boolean value) {
		Arrays.fill(includeFields, value);
	}


//    public abstract void save(String selection, String outFile)  throws Exception ;


	public void save(String selection, String outFile) throws Exception {
		save(selection, new FileOutputStream(outFile));
	}

	protected void save(String selection, OutputStream outStream) throws Exception {
		throw new RuntimeException("Saving to output stream is not supported for this save screen");
	}

    protected final void save_writeFile(FieldWriter writer, String selection)
    throws IOException{

    	if (commonSaveAsFields.treeExportChk.isSelected()) {
    		commonSaveAsFields.flatFileWriter.writeTree(
        			writer, commonSaveAsFields.getTreeFrame().getRoot(),
        			namesFirstLine.isSelected(),
        			! commonSaveAsFields.nodesWithDataChk.isSelected(),
        			commonSaveAsFields.getRecordFrame().getLayoutIndex());
        } else {
        	commonSaveAsFields.flatFileWriter.writeFile(
        			writer, namesFirstLine.isSelected(), commonSaveAsFields.getWhatToSave(selection));
        }
   	}

    public void edit(String outFile, String ext) {

		AbstractLayoutDetails layout = getEditLayout(ext, file.getLayout());
 
    	if (layout == null) {
    		String lcExt = ext.toLowerCase();
    		StandardLayouts genLayout = StandardLayouts.getInstance();
    		System.out.println(" --> getExtensionFor: >" + ext + "< " + lcExt + " " + ".csv".equals(lcExt));
	    	if (".xml".equals(lcExt) || ".xsl".equals(lcExt)) {
	    		layout = genLayout.getXmlLayout();
	    	} else if (".csv".equals(lcExt)) {
	        	layout = genLayout.getGenericCsvLayout();
	        }
    	}

    	if (layout == null) {
    		throw new RuntimeErrorException(null, "Can not edit the File: Can not determine the format");
    	} else {
    		//System.out.print(layout.getOption(Options.OPT_IS_TEXT_EDITTING_POSSIBLE));
    		FileView newFile = new FileView(layout,
    				ReIOProvider.getInstance(),
        			false);
    		StartEditor startEditor = new StartEditor(newFile, outFile, false, commonSaveAsFields.message ,0);

    		startEditor.doEdit();

    	}
    }

    public AbstractLayoutDetails getEditLayout(String ext, AbstractLayoutDetails l) {
    	return getEditLayout(ext);
    }

    public AbstractLayoutDetails getEditLayout(String ext) {
    	return null;
    }

    protected final List<AbstractLine> saveFile_getLines(String selection) {
    	return commonSaveAsFields.getViewToSave(selection).getLines();
    }


    protected final ScriptData getScriptData(String selection, String outFile) {
        AbstractLineNode root = null;
        String templateName = "";

        if (commonSaveAsFields.getTreeFrame() != null) {
        	root = commonSaveAsFields.getTreeFrame().getRoot();
        }

        if (template != null) {
        	templateName = template.getText();
        }

	   	return new ScriptData(
	   				saveFile_getLines(selection),
	   				commonSaveAsFields.file,
	        		root,
	        		onlyData.isSelected(), showBorder.isSelected(),
	        		commonSaveAsFields.getRecordFrame().getLayoutIndex(),
	        		outFile,
	        		ReFrame.getActiveFrame(),
	        		templateName);
    }


	/**
	 * @param layout the layout to set
	 */
	public void setRecordDetails(int[] fldLengths) {
		this.record = commonSaveAsFields.printRecordDetails;
		this.suppliedFieldLengths = fldLengths;

		includeFields = commonSaveAsFields.flatFileWriter.getFieldsToInclude();

		if (fldLengths != null) {
			rowCount = suppliedFieldLengths.length;
			fieldLengths = new int[rowCount];

			for (int i = 0; i < fieldLengths.length; i++) {
				fieldLengths[i] = NULL_INT;
			}

		}

		if (record != null) {
			AbstractLayoutDetails l = file.getLayout();
			rowCount = record.getFieldCount();
			fieldModel = new FldTblMdl();
			fieldTbl.setModel(fieldModel);

			if (DisplayType.isTreeStructure(l)) {
				rowCount = DisplayType.getMaxFields(l);
			}

			TableColumnModel tcm = fieldTbl.getColumnModel();
			tcm.getColumn(COL_INCLUDE).setCellRenderer(new CheckBoxTableRender());
			tcm.getColumn(COL_INCLUDE).setCellEditor(new DefaultCellEditor(new JCheckBox()));

			if (includeFields == null) {
				includeFields = new boolean[rowCount];
				setIncludeFields(true);
			}
			namesFirstLine.addChangeListener(new ChangeListener() {

				/* (non-Javadoc)
				 * @see javax.swing.event.ChangeListener#stateChanged(javax.swing.event.ChangeEvent)
				 */
				@Override
				public void stateChanged(ChangeEvent arg0) {
					fieldModel.fireTableDataChanged();
				}

			});
		}
	}



	protected final void setupPrintDetails(boolean isFixed) {
		AbstractLayoutDetails l = file.getLayout();
		int layoutIdx = file.getCurrLayoutIdx();
		int[] colLengths = null;
		commonSaveAsFields.printRecordDetails = null;

		switch (DisplayType.displayTypePrint(l, commonSaveAsFields.getRecordFrame().getLayoutIndex())) {
		case DisplayType.NORMAL:
			commonSaveAsFields.printRecordDetails = l.getRecord(layoutIdx);
			if (isFixed) {
				colLengths = getFieldWidths();
			}
			break;
		case DisplayType.PREFFERED:
			commonSaveAsFields.printRecordDetails = l.getRecord(DisplayType.getRecordMaxFields(l));
			if (isFixed) {
				colLengths = getFieldWidthsPrefered();
			}
			break;
		case DisplayType.HEX_LINE:
			colLengths = new int[1];
			colLengths[0] = l.getMaximumRecordLength() * 2;
			break;
		}

		setRecordDetails(colLengths);
	}

	public boolean isActive() {
		return true;
	}

	private int[] getFieldWidths() {
		AbstractLayoutDetails l = file.getLayout();
		int layoutIdx = file.getCurrLayoutIdx();
		int[] ret = new int[DisplayType.getFieldCount(l, layoutIdx)];
		int count = 0;
		Iterator<AbstractLine> it = file.iterator();

		while (it.hasNext()) {
			calcColLengthsForLine(ret, it.next(), l, layoutIdx);
			if (count++ > 30000) {
				break;
			}
		}

		return ret;
	}


	private int[] getFieldWidthsPrefered() {
		AbstractLayoutDetails l = file.getLayout();
		int layoutIdx = DisplayType.getRecordMaxFields(l);
		int[] ret = new int[l.getRecord(layoutIdx).getFieldCount()];
		int count = 0;
		Iterator<AbstractLine> it = file.iterator();
		AbstractLine line;

		while (it.hasNext()) {
			line = it.next();
			calcColLengthsForLine(ret, line, l, line.getPreferredLayoutIdx());
			if (count++ > 30000) {
				break;
			}
		}

		return ret;
	}

	/**
	 * @param text
	 * @see javax.swing.text.JTextComponent#setText(java.lang.String)
	 */
	public void setTemplateText(String text) {

		if (template != null) {
			template.setText(text);
		}
	}


	private void calcColLengthsForLine(
			int[] ret, AbstractLine line,
			AbstractLayoutDetails layout, int layoutIdx) {

		int colCount = layout.getRecord(layoutIdx).getFieldCount();
		calcLengths(ret, line, layoutIdx, 0, colCount);

		if (DisplayType.isTreeStructure(layout)) {
			int idx = DisplayType.getRecordMaxFields(layout);
			calcLengths(ret, line, idx, colCount, ret.length);
		}
	}

	private void calcLengths(int[] ret, AbstractLine line,
			int layoutIdx,
			int colStart, int colEnd) {
		Object o;
		for (int j = colStart; j < colEnd; j++) {
			o = line.getField(layoutIdx,  j);

			if (o != null) {
				ret[j] = Math.max(ret[j], o.toString().length());
			}
		}
	}


	@SuppressWarnings("serial")
	protected final  class FldTblMdl extends AbstractTableModel {

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#getColumnName(int)
		 */
		@Override
		public String getColumnName(int row) {

			return FIXED_COL_NAMES[row];
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#isCellEditable(int, int)
		 */
		@Override
		public boolean isCellEditable(int row, int col) {

			return col != COL_NAME;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#setValueAt(java.lang.Object, int, int)
		 */
		@Override
		public void setValueAt(Object val, int row, int col) {
			if (val != null) {
				switch (col) {
				case COL_INCLUDE:
					if (val instanceof Boolean) {
						includeFields[row] = ((Boolean) val).booleanValue();
					}
					break;
				case COL_LENGTH:
					try {
						int v = new Integer(val.toString().trim());
						if (v > 0) {
							fieldLengths[row] = v;
						}
					} catch (Exception e) {

					}

					break;
				}
			}

		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getColumnCount()
		 */
		@Override
		public int getColumnCount() {
			return FMT_TO_NUMBER_OF_COLS[panelFormat];
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getRowCount()
		 */
		@Override
		public int getRowCount() {
			return includeFields.length;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getValueAt(int, int)
		 */
		@Override
		public Object getValueAt(int row, int col) {
			Object ret = null;

			try {
			switch (col) {
			case COL_NAME:
				if (record == null || row >= record.getFieldCount()) {
					ret = "Column " + row;
				} else {
					ret = record.getField(row).getName();
				}
				break;
			case COL_INCLUDE:
				if (includeFields != null) {
					ret = Boolean.valueOf(includeFields[row]);
				}
				break;
			case COL_LENGTH:
				if (suppliedFieldLengths != null) {
					int v = suppliedFieldLengths[row];

					if (fieldLengths[row] > 0) {
						v = fieldLengths[row];
					} else if (namesFirstLine.isSelected() && record != null) {
						v = Math.max(
								suppliedFieldLengths[row],
								record.getField(row).getName().length());
					}
					ret = Integer.valueOf(v);
				}
				break;
			}
			} catch (Exception e) {
				e.printStackTrace();
			}

			return ret;
		}

	}

	
	protected class SelectAction implements ActionListener {
		final boolean value;

		protected SelectAction(boolean value) {
			this.value = value;
		}

		/* (non-Javadoc)
		 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
		 */
		@Override
		public void actionPerformed(ActionEvent e) {
			setIncludeFields(value);
			fieldModel.fireTableDataChanged();
		}
		
	}

}
