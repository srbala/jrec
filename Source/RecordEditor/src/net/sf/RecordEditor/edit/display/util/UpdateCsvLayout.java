package net.sf.RecordEditor.edit.display.util;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.AbstractAction;
import javax.swing.DefaultCellEditor;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JMenu;
import javax.swing.JTable;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.TableColumnModel;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.FieldDetail;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.Types.Type;
import net.sf.RecordEditor.edit.util.ReMessages;
import net.sf.RecordEditor.re.display.AbstractFileDisplay;
import net.sf.RecordEditor.re.display.IChildDisplay;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.MenuPopupListener;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.lang.ReAbstractAction;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.CheckBoxTableRender;
import net.sf.RecordEditor.utils.swing.ComboBoxRender;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.ComboBoxs.DelimiterCombo;
import net.sf.RecordEditor.utils.swing.ComboBoxs.QuoteCombo;

public class UpdateCsvLayout implements ActionListener, IChildDisplay {

	private static final String NUMBER_FIXED_DECIMAL
			= LangConversion.convertComboItms("Csv Field Types Fixed", "Number (Fixed Decimal)");

	private static final String TEXT_FIELD = LangConversion.convertComboItms("Csv Field Types Text", "Text");


	private static final String[] COL_NAMES = LangConversion.convertColHeading(
			"Update Csv File Format",
			new String[] {
		"Field Name", "Include", "Type", "Decimal Places", "Source Column",
		"Default"
	});
	private static final int FIELD_COL = 0;
	private static final int INCLUDE_COL = 1;
	private static final int TYPE_COL = 2;
	private static final int DECIMAL_COL = 3;
	private static final int SOURCE_COL = 4;
	private static final int DEFAULT_COL = 5;
	//private static final int DEFAULT_IN_EMPTY_COL = 6;

	private static final String[] TYPES_TEXT = LangConversion.convertComboItms(
			"Csv Field Types",
			new String[] {
		TEXT_FIELD,
		LangConversion.convertComboItms("Csv Field Types Multi-Line", "Multi Line Text"),
		LangConversion.convertComboItms("Csv Field Types Html", "Html Field"),
		LangConversion.convertComboItms("Csv Field Types Num", "Number"),
		NUMBER_FIXED_DECIMAL
	});
	private static final int[] TYPE = {
		Type.ftChar, Type.ftMultiLineEdit, Type.ftHtmlField,
		Type.ftNumAnyDecimal, Type.ftNumLeftJustified,
	};

	private ArrayList<FieldDef> fields = new ArrayList<FieldDef>(20);
	private LayoutDetail layout;

	private FileView view;
	private AbstractFileDisplay source;

	//private BasePanel panel = new BasePanel();
	private FieldModel fieldModel = new FieldModel();
	private JTable fieldTbl = new JTable(fieldModel);
	private DelimiterCombo delimiterCombo;
	private QuoteCombo quoteCombo = QuoteCombo.newCombo();
	private JButton goBtn = SwingUtils.newButton("Apply");

	private JMenu moveMenu = SwingUtils.newMenu("Move ...");

	private MenuPopupListener popupListner = new MenuPopupListener();
	private ReFrame frame;

	private String delimiter, quote;
	private int /*delimiterIdx,*//* quoteIdx,*/ newFieldCount;
	private boolean allowTypeUpdates = true;

	//private boolean showSourceColumn = false;

	public UpdateCsvLayout(AbstractFileDisplay activeScreen) {

		source = (AbstractFileDisplay) activeScreen;
		view = source.getFileView();
		if (view.isSimpleCsvFile()
		&&  view.getLayout() instanceof LayoutDetail) {
			layout = (LayoutDetail) view.getLayout();

			init_setupFieldList();

			init_setupScreen();
		}
	}

	private void init_setupFieldList() {
		RecordDetail rec = layout.getRecord(0);
		FieldDetail f;
		boolean found;
		String typeStr;

		for (int i = 0; i < rec.getFieldCount(); i++) {
			f = rec.getField(i);

			found = false;
			typeStr = "";
			for (int j = 0; j < TYPE.length; j++) {
				if (f.getType() == TYPE[j]) {
					found = true;
					typeStr = TYPES_TEXT[j];
					break;
				}
			}
			if (! found) {
				this.allowTypeUpdates = false;
			}
			fields.add(
					new FieldDef(i, f.getName(), typeStr, f.getDecimal(), f.getDefaultValue())
			);
		}
	}

	private void init_setupScreen() {
		BasePanel pnl = new BasePanel();
		delimiter  = layout.getDelimiterDetails().jrDefinition();
		quote  = layout.getRecord(0).getQuote();

		init_setupTablePopup();

		if (layout.getFileStructure() == Constants.IO_UNICODE_TEXT
		||  layout.getFileStructure() == Constants.IO_UNICODE_NAME_1ST_LINE) {
			delimiterCombo = DelimiterCombo.NewTextDelimCombo();
		} else {
			delimiterCombo = DelimiterCombo.NewDelimCombo();
		}

//		System.out.println(" ~~!!~~ 1 " + delimiterCombo.getSelectedIndex() + " " + delimiterCombo.getItemCount());
		delimiterCombo.ensureDelimitierExists(delimiter);// getIndex(delim, Common.FIELD_SEPARATOR_LIST1_VALUES, delimiterCombo);
//		System.out.println(" ~~!!~~ 2 " + delimiterCombo.getSelectedIndex() + " " + delimiterCombo.getItemCount());

		quoteCombo.setText(quote);
		
				//getIndex(quote, Common.QUOTE_VALUES, quoteCombo);


		setupTable();

		pnl.addComponentRE(1, 5, 300, BasePanel.GAP,
		        BasePanel.FULL, BasePanel.FULL,
		        fieldTbl);
		pnl.setComponentName(fieldTbl, "FieldChange");

		pnl.setGapRE(BasePanel.GAP2);
		pnl.addLineRE("Field Delimiter", delimiterCombo);
		pnl.addLineRE("Quote", quoteCombo);

		pnl.addLineRE(null, null, this.goBtn);

		frame = new ReFrame(
						view.getFileNameNoDirectory(),
						"Update Screen Columns",
						view);
		frame.setDefaultCloseOperation(ReFrame.DISPOSE_ON_CLOSE);
		frame.addMainComponent(pnl);
		frame.setVisible(true);
		frame.setToMaximum(false);

		goBtn.addActionListener(this);
		fieldTbl.addMouseListener(popupListner);
	}

//	private int getIndex(String value, String[] list, JComboBox combo) {
//
//		int idx = Common.NULL_INTEGER;
//		for (int i = list.length-1; i >= 0; i--) {
//			if (list[i].equals(value)) {
//				combo.setSelectedIndex(i);
//				idx = i;
//				break;
//			}
//		}
//		if (idx < 0) {
//			idx = combo.getItemCount();
//			combo.addItem(value);
//			combo.setSelectedIndex(idx);
//		}
//		return idx;
//	}

	private void init_setupTablePopup() {
		popupListner.setTable(fieldTbl);
		popupListner.getPopup().add(moveMenu);
		popupListner.getPopup().add(new AddAction(false, "Add Field Before"));
		popupListner.getPopup().add(new AddAction(true, "Add Field After"));

		setupFieldMenus();
	}

	private void setupFieldMenus() {
		//RecordDetail rec = layout.getRecord(0);

		moveMenu.removeAll();
		moveMenu.add(new MoveAction(0, ReMessages.BEFORE_FIELD.get(fields.get(0).name)));

		for (int i = 0; i < fields.size(); i++) {
			moveMenu.add(new MoveAction(i+1, ReMessages.AFTER_FIELD.get(fields.get(i).name)));
		}
	}

	private void setupTable() {

		TableColumnModel tcm = fieldTbl.getColumnModel();
		RecordDetail rec = layout.getRecord(0);
		String[] allFields = new String[rec.getFieldCount() + 1];
		allFields[0] = "";
		for (int i = rec.getFieldCount() - 1; i>= 0; i--) {
			allFields[i+1] = rec.getField(i).getName();
		}

		tcm.getColumn(INCLUDE_COL).setCellRenderer(new CheckBoxTableRender());
		tcm.getColumn(INCLUDE_COL).setCellEditor(new DefaultCellEditor(new JCheckBox()));

		tcm.getColumn(TYPE_COL).setCellRenderer(new ComboBoxRender(TYPES_TEXT));
		tcm.getColumn(TYPE_COL).setCellEditor(new DefaultCellEditor(new JComboBox(TYPES_TEXT)));

		tcm.getColumn(SOURCE_COL).setCellRenderer(new ComboBoxRender(allFields));
		tcm.getColumn(SOURCE_COL).setCellEditor(new DefaultCellEditor(new JComboBox(allFields)));

		Common.calcColumnWidths(fieldTbl, 0);
		fieldTbl.setRowHeight(SwingUtils.COMBO_TABLE_ROW_HEIGHT);
	}


	/* (non-Javadoc)
	 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
	 */
	@Override
	public void actionPerformed(ActionEvent arg0) {

		Common.stopCellEditing(fieldTbl);
		if (isUpdateExistingLayout()) {
			//System.out.println("~~ Update Exisiting !!!");
			FieldDef f;
			RecordDetail rec = layout.getRecord(0);
			for (int i = 0; i < fields.size(); i++) {
				f = fields.get(i);

				rec.getField(i).setNameType(f.name, getType(f));
	            if (f.defaultValue != null && ! "".equals(f.defaultValue.trim())) {
	            	rec.getField(i).setDefaultValue(f.defaultValue);
	            }
			}
			Code.notifyFramesOfUpdatedLayout(view.getBaseFile(), layout);
			//view.getBaseFile().setLayout(layout);
		} else {
			//System.out.println("~~ Update with new  !!!");
			LayoutDetail newLayout = buildNewLayout();
			int[] trans = getFieldTranslation();

			Code.updateFile(view.getBaseFile(), newLayout, trans);
			view.getBaseFile().setLayout(newLayout);
		}
		frame.doDefaultCloseAction();
		frame.setVisible(false);
	}

	private boolean isUpdateExistingLayout() {
		boolean ret = true;
		FieldDef f;

//		System.out.println( " !!! 1 " + delimiter + " " + delimiterCombo.getDelimiter());
//		System.out.println( " !!! 2 " + quote + " " + quoteCombo.getQuote());
		if ( (! delimiterCombo.getDelimiter().equalsIgnoreCase(delimiter))
		||   (! quoteCombo.getQuote().equals(quote))) {
			ret = false;
		} else {
			for (int i = 0; i < fields.size(); i++) {
				f = fields.get(i);

				if ((f.include && (f.originalPos != i))
				||  ((! f.include) && f.originalPos >= 0)
				||  (  NUMBER_FIXED_DECIMAL.equals(f.type)
					&& (! f.type.equals(f.originalType) || f.decimal != f.originalDecimal))
				) {
					ret = false;
					break;
				}
			}
		}
		System.out.println( " !!! 3 " + ret);

		return ret;
	}


	private LayoutDetail buildNewLayout() {
		newFieldCount = 0;

		for (int i = 0; i < fields.size(); i++) {
			if (fields.get(i).include) {
				newFieldCount += 1;
			}
		}

		RecordDetail.FieldDetails[] flds = new RecordDetail.FieldDetails[newFieldCount];
        RecordDetail[] recs = new RecordDetail[1];
        int format    = 0;
        FieldDef f;
        RecordDetail rec = layout.getRecord(0);
        int j = 0;

        String quote = rec.getQuote();

        //if (quoteCombo.getSelectedIndex() < Common.QUOTE_VALUES.length) {
        	quote = quoteCombo.getKeyValue();
        			//Common.QUOTE_VALUES[quoteCombo.getSelectedIndex()];
        //}

	    for (int i = 0; i < fields.size(); i++) {
	    	f = fields.get(i);
	    	if (f.include) {
	            flds[j] = new RecordDetail.FieldDetails(f.name, f.name, getType(f), f.decimal,
	                        layout.getFontName(), format, "");
	            flds[j].setPosOnly(j + 1);
	            if (f.defaultValue != null && ! "".equals(f.defaultValue.trim())) {
	            	flds[j].setDefaultValue(f.defaultValue);
	            }
	            j += 1;
	    	}
	    }

        recs[0] = new RecordDetail(
        		rec.getRecordName(), "", "", rec.getRecordType(),
        		delimiterCombo.getDelimiter(), quote,
        		layout.getFontName(), flds, rec.getRecordStyle(), 0);

        return
            new LayoutDetail(layout.getLayoutName(), recs, "",
                layout.getLayoutType(),
                layout.getRecordSep(), "", layout.getFontName(), null,
                layout.getFileStructure()
            );
	}

	private int[] getFieldTranslation() {
		int[] ret = new int[newFieldCount];
		FieldDef f;
		int j = 0;

		for (int i = 0; i < fields.size(); i++) {
		   	f = fields.get(i);
		   	if (f.include) {
		   		ret[j] = f.sourceField;
		   		j += 1;
		   	}
		}
		return ret;
	}

	private int getType(FieldDef field) {
		int type = Type.ftChar;
		for (int j = 0; j < TYPES_TEXT.length; j++) {
			if (TYPES_TEXT[j].equals(field.type)) {
				type = TYPE[j];
				break;
			}
		}
		return type;
	}



	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.re.display.IChildDisplay#getSourceDisplay()
	 */
	@Override
	public AbstractFileDisplay getSourceDisplay() {
		return source;
	}



	private static class FieldDef {
		public final int originalPos, originalDecimal;
		public final String originalType;
		public int sourceField, decimal;
		public Boolean include = Boolean.TRUE;
		public String name;
		public String type;
//		public String source = "";
		public String defaultValue = "";
		//public Boolean defaultInEmpty = Boolean.TRUE;

		public FieldDef(int row) {
			this(Constants.NULL_INTEGER, Integer.toString(row+1), TEXT_FIELD, 0, null);
		}

		public FieldDef(int originalPos, String name,
				String type, int decimal, Object defaultVal) {
			super();
			this.sourceField = originalPos;
			this.originalPos = originalPos;
			this.name = name;
			this.type = type;
			this.originalType = type;
			this.decimal = decimal;
			this.originalDecimal = decimal;

			if (defaultVal != null) {
				defaultValue = defaultVal.toString();
			}
		}
	}

	private void fireFieldTblChanged() {
		fieldModel.fireTableDataChanged();
		setupFieldMenus();

	}

	@SuppressWarnings("serial")
	private class FieldModel extends AbstractTableModel {

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#getColumnName(int)
		 */
		@Override
		public String getColumnName(int col) {
			return COL_NAMES[col];
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#isCellEditable(int, int)
		 */
		@Override
		public boolean isCellEditable(int row, int col) {

			FieldDef f = fields.get(row);
			switch (col) {
			case DECIMAL_COL:	return NUMBER_FIXED_DECIMAL.equals(f.type);
			case TYPE_COL:		return allowTypeUpdates;
			}

			return col < SOURCE_COL
				|| col >= DEFAULT_COL
				|| f.originalPos < 0;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.AbstractTableModel#setValueAt(java.lang.Object, int, int)
		 */
		@Override
		public void setValueAt(Object val, int row, int col) {
			FieldDef f = fields.get(row);

			switch (col) {
			case FIELD_COL:
				if (val == null || "".equals(val.toString())) {
					f.name = Integer.toString(row);
				} else {
					f.name = val.toString();
				}
				break;
			case INCLUDE_COL:	f.include = (Boolean) val;		break;
			case TYPE_COL:		f.type = val.toString();		break;
			case DECIMAL_COL:
				if (val == null || "".equals(val.toString())) {
					f.decimal = 0;
				} else if (val instanceof Integer) {
					f.decimal = ((Integer) val).intValue();
				} else {
					try {
						f.decimal = Integer.parseInt(val.toString());
					} catch (Exception e) {
						// TODO: handle exception
					}
				}
				break;
			case SOURCE_COL:
				if (val == null || "".equals(val.toString())) {
					f.sourceField = Constants.NULL_INTEGER;
				} else {
					f.sourceField = layout.getRecord(0).getFieldIndex(val.toString());
				}
				break;
			case DEFAULT_COL:
				if (val == null) {
					f.defaultValue = "";
				} else {
					f.defaultValue = val.toString();
				}

			}
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getColumnCount()
		 */
		@Override
		public int getColumnCount() {
			return COL_NAMES.length;
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getRowCount()
		 */
		@Override
		public int getRowCount() {
			return fields.size();
		}

		/* (non-Javadoc)
		 * @see javax.swing.table.TableModel#getValueAt(int, int)
		 */
		@Override
		public Object getValueAt(int row, int col) {
			Object ret = null;
			FieldDef f = fields.get(row);

			switch (col) {
			case FIELD_COL:		ret = f.name;		break;
			case INCLUDE_COL:	ret = f.include;	break;
			case TYPE_COL:		ret = f.type;		break;
			case DECIMAL_COL:
				if (NUMBER_FIXED_DECIMAL.equals(f.type)) {
					ret = Integer.valueOf(f.decimal);
				}
				break;
			case SOURCE_COL:
				ret = "";
				if (f.originalPos < 0 && f.sourceField >= 0) {
					ret = layout.getRecord(0).getField(f.sourceField).getName();
				}
				break;
			case DEFAULT_COL:	ret = f.defaultValue;		break;
			//case DEFAULT_IN_EMPTY_COL:	ret = f.defaultInEmpty;		break;
			}

			return ret;
		}

	}

	@SuppressWarnings("serial")
	private class MoveAction extends AbstractAction {
		int destination;


		public MoveAction(int destination, String name) {
			super(name);
			this.destination = destination;
		}


		/* (non-Javadoc)
		 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
		 */
		@Override
		public void actionPerformed(ActionEvent arg0) {
			int sourceRow = popupListner.getPopupRow();
			FieldDef f = fields.get(sourceRow);

			Common.stopCellEditing(fieldTbl);
			if (sourceRow < destination) {
				if (destination >= fields.size()) {
					fields.add(f);
				} else {
					fields.add(destination, f);
				}
				fields.remove(sourceRow);

				fireFieldTblChanged();
			} else if (sourceRow > destination){
				fields.remove(sourceRow);
				fields.add(destination, f);

				fireFieldTblChanged();
			}
		}
	}

	@SuppressWarnings("serial")
	private class AddAction extends ReAbstractAction {
		boolean after;


		public AddAction(boolean after, String name) {
			super(name);
			this.after = after;
		}


		/* (non-Javadoc)
		 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
		 */
		@Override
		public void actionPerformed(ActionEvent arg0) {
			int destination = popupListner.getPopupRow();
			FieldDef f;
			Common.stopCellEditing(fieldTbl);

			if (after) {
				destination += 1;
			}
			f = new FieldDef(destination);

			if (destination >= fields.size()) {
				fields.add(f);
			} else {
				fields.add(destination, f);
			}

			fireFieldTblChanged();
		}
	}
}
