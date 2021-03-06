package net.sf.RecordEditor.edit.util;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JInternalFrame;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.AbstractTableModel;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.CsvParser.CsvParserManagerChar;
import net.sf.JRecord.Details.AbstractLine;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.Line;
import net.sf.JRecord.Details.LineProvider;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.JRecord.Types.Type;
import net.sf.RecordEditor.re.display.DisplayBuilderFactory;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.charsets.FontCombo;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.edit.ManagerRowList;
import net.sf.RecordEditor.utils.fileStorage.DataStoreStd;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.BmKeyedComboBox;
import net.sf.RecordEditor.utils.swing.BmKeyedComboModel;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.ComboBoxs.DelimiterCombo;
import net.sf.RecordEditor.utils.swing.ComboBoxs.QuoteCombo;


/**
 * Create a Csv File
 * @author Bruce Martin
 *
 */
public class NewCsvFile {

	private static int[][] STRUCTURES = {
		{Constants.IO_BIN_TEXT, Constants.IO_BIN_NAME_1ST_LINE},
		{Constants.IO_UNICODE_TEXT, Constants.IO_UNICODE_NAME_1ST_LINE},
	};

	public final ReFrame frame;
	public final BaseHelpPanel panel = new BaseHelpPanel();

	private BmKeyedComboModel styleModel = new BmKeyedComboModel(new ManagerRowList(
			CsvParserManagerChar.getInstance(), false));

	private ColumnNameMdl colNameMdl = new ColumnNameMdl();

	private NumField   rowFld		 = new NumField("row", 5, null);
	private NumField   colFld		 = new NumField("row", 3, colNameMdl);

	private JCheckBox  namesChk		 = new JCheckBox();
	private JCheckBox  unicodeChk	 = new JCheckBox();
	private FontCombo  fontCombo	 = new FontCombo();
	private DelimiterCombo fieldSep  = DelimiterCombo.NewDelimCombo();
	private QuoteCombo  quote		 = QuoteCombo.newCombo();
    private BmKeyedComboBox parser   = new BmKeyedComboBox(styleModel, false);

	//private JLabel     colNamesLbl   = new JLabel("Column Names:");
	private JTable     colNamesTbl	 = new JTable(colNameMdl);

	private JButton    goBtn	     = SwingUtils.newButton("Create");

	private JTextField msgTxt	     = new JTextField();

	private ArrayList<String> columnNames = new ArrayList<String>();

	public NewCsvFile() {
		this(new ReFrame("","New Csv File", null));
	}

	public NewCsvFile(ReFrame displayFrame) {
		frame = displayFrame;
		init_100_Setup();
		init_200_LayoutScreen();
		init_300_Listners();

		frame.setVisible(true);
	}

	private void init_100_Setup() {

		namesChk.setSelected(true);
	}

	private void init_200_LayoutScreen() {

		panel	.setGapRE(BasePanel.GAP2)
			.addLineRE(               "Rows", rowFld.field)
			.addLineRE(               "Cols", colFld.field)
			.addLineRE("Names on First Line", namesChk)
			.addLineRE(            "Unicode", unicodeChk)
			.addLineRE(               "Font", fontCombo)
			.addLineRE(    "Field Seperator", fieldSep)
			.addLineRE(              "Quote", quote)
			.addLineRE(             "Parser", parser)
				//.setGapRE(BasePanel.GAP1)
			
			.addComponentRE(1, 3, SwingUtils.TABLE_ROW_HEIGHT * 10,
		        BasePanel.GAP1,
		        BasePanel.FULL, BasePanel.FULL,
		        colNamesTbl)
			.addLineRE(null, null, goBtn)
				.setGapRE(BasePanel.GAP1)
			.addMessage(msgTxt)
				.setHeightRE(BasePanel.HEIGHT_1P6);

		frame.addMainComponent(panel);
		frame.setDefaultCloseOperation(JInternalFrame.DISPOSE_ON_CLOSE);
	}



	private void init_300_Listners() {

		namesChk.addActionListener(new ActionListener() {
			@Override public void actionPerformed(ActionEvent e) {
				boolean visible = namesChk.isSelected();

				colNamesTbl.setVisible(visible);
			}
		});

		goBtn.addActionListener(new ActionListener() {
			@Override public void actionPerformed(ActionEvent e) {
				Common.stopCellEditing(colNamesTbl);
				editFile();

				frame.setVisible(false);
			}
		});
	}

	@SuppressWarnings("unchecked")
	private void editFile() {
		LayoutDetail layout = getLayout();
		AbstractLine l;
		DataStoreStd<AbstractLine> store = DataStoreStd.newStore(layout);
		LineProvider<LayoutDetail, Line> p = LineIOProvider.getInstance()
										.getLineProvider(layout);
		for (int i = 0; i < rowFld.value; i++) {
			l = p.getLine(layout);
			try {
				l.setField(0, colFld.value - 1, "");
			} catch (Exception e) {
			}
			store.add(l);
		}

		FileView file = new FileView(
				store,
				null,
				null,
				false);
		DisplayBuilderFactory.getInstance().newDisplay(DisplayBuilderFactory.ST_INITIAL_EDIT, "", null, file.getLayout(), file, 0);
	}

	private LayoutDetail getLayout() {
		LayoutDetail layout;
		int i;
		String s;
		byte[] eol = Common.SYSTEM_EOL_BYTES;
		String font = fontCombo.getText();
		String q   = quote.getQuote();
		String sep = fieldSep.getDelimiter();
		int structure = STRUCTURES[toInt(unicodeChk.isSelected())]
		                          [toInt(namesChk.isSelected())];
		RecordDetail.FieldDetails[] flds = new RecordDetail.FieldDetails[colFld.value];
	    RecordDetail[] recs = new RecordDetail[1];

	    for (i = 0; i < colFld.value; i++) {
		    s = columnNames.get(i);
            flds[i] = new RecordDetail.FieldDetails(s, s, Type.ftChar, 0,
                        font, 0, "");
            flds[i].setPosOnly(i + 1);
	    }

        recs[0] = new RecordDetail(Common.GENERATED_CSV_SCHEMA_NAME, "", "", Constants.rtDelimited,
        		sep, q, font, flds,
        		((Integer)parser.getSelectedItem()).intValue(), 0);

        if (font != null && font.length() > 0) {
        	try {
				eol = "\n".getBytes(font);
			} catch (UnsupportedEncodingException e) {
			}
        }

        layout  =
            new LayoutDetail("GeneratedCsv", recs, "",
                Constants.rtDelimited,
                eol, "", font, null,
                structure
            );

		return layout;
	}

	private int toInt(boolean b) {
		int ret = 0;
		if (b) {
			ret = 1;
		}
		return ret;
	}
//  ===========================================================

	private class NumField extends FocusAdapter {
		public int value;
		public JTextField field = new JTextField();
		private final String name;
		private final AbstractTableModel mdl;

		public NumField(String fieldName, int initialValue, AbstractTableModel model) {
			name = fieldName;
			value = initialValue;
			field.addFocusListener(this);
			mdl = model;
			field.setText(Integer.toString(value));
		}

		/* (non-Javadoc)
		 * @see java.awt.event.FocusAdapter#focusLost(java.awt.event.FocusEvent)
		 */
		@Override
		public void focusLost(FocusEvent evt) {
			try {
				int lastValue = value;
				value = Integer.parseInt(field.getText());

				if (mdl != null && lastValue != value && namesChk.isSelected()) {
					mdl.fireTableDataChanged();
				}
			} catch (Exception ex) {
				msgTxt.setText(LangConversion.convert("Invalid number in {0}, msg=", name) + ex.getMessage());
			}
		}
	}



	@SuppressWarnings("serial")
	private class ColumnNameMdl extends AbstractTableModel {

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getColumnCount()
		 */
		@Override
		public int getColumnCount() {
			return 1;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getRowCount()
		 */
		@Override
		public int getRowCount() {
			return colFld.value;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getValueAt(int, int)
		 */
		@Override
		public Object getValueAt(int rowIndex, int columnIndex) {
			String s = "";

			if (rowIndex < columnNames.size()) {
				s = columnNames.get(rowIndex);
			}

			return s;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#getColumnName(int)
		 */
		@Override
		public String getColumnName(int column) {
			return "Column Name";
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#isCellEditable(int, int)
		 */
		@Override
		public boolean isCellEditable(int rowIndex, int columnIndex) {
			return true;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#setValueAt(java.lang.Object, int, int)
		 */
		@Override
		public void setValueAt(Object value, int rowIndex, int columnIndex) {
			String s  = "";
			if (value != null) {
				s = value.toString();
			}
			while (rowIndex >= columnNames.size()) {
				columnNames.add("");
			}
			columnNames.set(rowIndex, s);
		}


	}
}
