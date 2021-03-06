package net.sf.RecordEditor.layoutEd.panels;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

import net.sf.JRecord.Common.Constants;
import net.sf.RecordEditor.re.db.Combo.ComboRec;
import net.sf.RecordEditor.re.db.Combo.ComboValuesDB;
import net.sf.RecordEditor.re.db.Combo.ComboValuesRec;
import net.sf.RecordEditor.re.db.Table.TableDB;
import net.sf.RecordEditor.re.db.Table.TableRec;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.common.ReConnection;
import net.sf.RecordEditor.utils.jdbc.DBComboModel;
import net.sf.RecordEditor.utils.jdbc.DBtableModel;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.screenManager.ReMainFrame;
import net.sf.RecordEditor.utils.swing.AbsJTable;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.BmKeyedComboBox;

@SuppressWarnings("serial")
public class ComboPnl extends BaseHelpPanel implements ActionListener {



	//private JTextField sfCombo_Id = new JTextField();
	private static final String[] COLUMN_TYPE_LIST = LangConversion.convertComboItms(
			"Combo Options",
			new String[] {"Standard Combo", "Key / Value Combo"});

	private TableDB systemTable = new TableDB();
	private DBComboModel<TableRec> systemModel = new DBComboModel<TableRec>(systemTable, 0, 1 , false, false);
	private BmKeyedComboBox sfSystem;
	private JTextField sfComboName = new JTextField();
	private JComboBox sfColumnType = new JComboBox(COLUMN_TYPE_LIST);

	private JTextField message = new JTextField();

	private TableUpdatePnl<ComboValuesRec> updateOptions;

	private String msgText = "";
	private ComboRec currVal;
	private int connectionIdx;

	private ComboValuesDB valuesDB = new ComboValuesDB();

	private DBtableModel<ComboValuesRec> comboDetailsModel;
	private AbsJTable comboDetails;

	public  ComboPnl(ComboRec value, int connectionIndex) {
		super();

		connectionIdx = connectionIndex;

		init_100_setupScreenFields();
		setValues(value);

		//addComponent("Combo_Id", sfCombo_Id);
		addLineRE("System", sfSystem);
		addLineRE("Combo_Name", sfComboName);
		addLineRE("Combo Type", sfColumnType);
		setGapRE(BasePanel.GAP0);
		updateOptions = new TableUpdatePnl<ComboValuesRec>(this, null);

		addComponentRE(1, 3, BasePanel.FILL, BasePanel.GAP,
				BasePanel.FULL, BasePanel.FULL,
				comboDetails);

		addMessage(message);

		updateOptions.setTableDtls(comboDetailsModel, comboDetails, new ComboValuesRec());
	}

	private void init_100_setupScreenFields() {
		ReConnection con = new ReConnection(connectionIdx);

		this.setHelpURLre(Common.formatHelpURL(Common.HELP_COMBO_EDIT));

		systemTable.setConnection(con);
		systemTable.setParams(3);
		sfSystem = new BmKeyedComboBox(systemModel, false);

		valuesDB.setConnection(con);
		//valuesDB.setParams(currVal.getComboId());

		comboDetailsModel = new DBtableModel<ComboValuesRec>(ReMainFrame.getMasterFrame(), valuesDB);
		comboDetailsModel.setCellEditable(true);

		comboDetails = new AbsJTable(comboDetailsModel);

		sfColumnType.addActionListener(this);
	}



	/**
	 *  This method sets the value of the Screen values from the values in  Val.
	 *
	 *  @param val holds the values to be assigned to screen fields
	 */
	public void setValues(ComboRec val) {

		currVal = val;
		if (val == null) {
			//sfSystem.setSelectedItem(0);
			sfComboName.setText("");
			sfColumnType.setSelectedIndex(0);
			valuesDB.setParams(Constants.NULL_INTEGER);
			comboDetailsModel.removeAll();
		} else {
			sfSystem.setSelectedItem(Integer.valueOf(val.getSystem()));
			sfComboName.setText(val.getComboName());
			sfColumnType.setSelectedIndex(val.getColumnType() - 1);
			valuesDB.setParams(currVal.getComboId());
			comboDetailsModel.load();
		}
		valuesDB.setColumnCount(sfColumnType.getSelectedIndex() + 1);
		comboDetailsModel.fireTableStructureChanged();
	}


	/**
	 * Clone and return the current record
	 * @return cloned record
	 */
	public ComboRec getClone(String newName) {
		ComboRec ret = null;
		ComboRec temp = getValues();

		if (temp.isUpdateSuccessful()) {
			ComboValuesRec rec;
			int numRecs = comboDetailsModel.getRowCount();

			ret = (ComboRec) temp.clone();
			ret.setComboName(newName);
			sfComboName.setText(newName);

			for (int i = 0; i < numRecs; i++) {
				rec = (ComboValuesRec) comboDetailsModel.getRecord(i).clone();
				rec.setNew(true);
				rec.setUpdateStatus(ComboValuesRec.UPDATED);
				comboDetailsModel.setRecord(i, rec);
			}
			currVal = ret;
		}

		return ret;
	}


	/**
	 *  This method gets the Screen values as a ComboListRec
	 *
	 *  @return values of screen fields as a ComboListRec
	 */
	public ComboRec getValues() {
		String fld="";

		if (currVal == null) {
			currVal = new ComboRec();
		}

		try {
			currVal.setUpdateSuccessful(true);
			fld = "System";
			currVal.setSystem(((Integer) sfSystem.getSelectedItem()).intValue());
			fld = "Combo_Name";
			currVal.setComboName(sfComboName.getText());
			fld = "Column_Type";
			currVal.setColumnType(sfColumnType.getSelectedIndex() + 1);
		} catch (Exception ex) {
			currVal.setUpdateSuccessful(false);
			setMessage(LangConversion.convert("Invalid Field") + " "  + fld + " - " + ex.getMessage());
		}
		return currVal;
	}

	/**
	 * Save Combo Items back to the DB
	 */
	public void saveItems() {
		valuesDB.setParams(currVal.getComboId());
		comboDetailsModel.updateDB();
	}


	private void setMessage(String msg) {
		message.setText(msg);
		msgText = msg;
	}

	/**
	 *  Get the error Message
	 */
	public String getMsg() {
		return msgText;
	}

	/**
	 * Stop cell editing
	 *
	 */
	public void stopCellEditing() {
	    Common.stopCellEditing(comboDetails);
	}


	/**
	 * Get action handler for editing Table lines
	 *
	 * @return requested action handler
	 */
	public ReActionHandler getLinesActionHandler() {
	    return updateOptions;
	}


	/**
	 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
	 */
	public void actionPerformed(ActionEvent event) {

		if (event.getSource() == sfColumnType) {
			valuesDB.setColumnCount(sfColumnType.getSelectedIndex() + 1);
			comboDetailsModel.fireTableStructureChanged();
		}

	}



	/**
	 * Check if the user really wants to delete a record Layout
	 * @return wether to delete the layout
	 */
	public final boolean isOkToDelete() {
		boolean ret = false;

		if (currVal != null) {
			int result = JOptionPane.showConfirmDialog(null,
					LangConversion.convert("Are you sure you want to delete Combo: {0}", sfComboName.getText()),
					LangConversion.convert("Delete: {0}", sfComboName.getText()),
					JOptionPane.YES_NO_OPTION);

			ret = result == JOptionPane.YES_OPTION;
			if (ret) {
				valuesDB.setParams(currVal.getComboId());
				valuesDB.deleteAll();
			}
		}
		return true;
	}
}
