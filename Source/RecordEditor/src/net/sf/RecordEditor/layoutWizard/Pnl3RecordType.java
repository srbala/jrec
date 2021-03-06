/*
 * @Author Bruce Martin
 * Created on 8/01/2007
 *
 * Purpose:
 * 2nd wizard screen where the user selects the starting
 * position of every field in the file
 *
 * Changes
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Name changes, remove done method call
 *   - JRecord creation changes
 *
 * # Version 0.61b Bruce Martin 2007/05/05
 *  - Changes o support user selecting the default type
 *  - Changing Column heading from "" to " " so it will be
 *    displayed under Windows look and Feel
 *
 */
package net.sf.RecordEditor.layoutWizard;

import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JEditorPane;
import javax.swing.JTextField;
import javax.swing.text.JTextComponent;

import net.sf.RecordEditor.re.util.BuildTypeComboList;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.swing.AbsRowList;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeCombo;

/**
 * 2nd wizard screen where the user selects the starting
 * position of every field in the file
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class Pnl3RecordType extends WizardPanel {

    private static final int FILE_HEIGHT =  SwingUtils.TABLE_ROW_HEIGHT * 15 - 3;

    private JEditorPane tips;

    private JTextField nameTxt = new JTextField();
    private JTextField startTxt = new JTextField();
    private JTextField lengthTxt = new JTextField();
    private TreeCombo typeCombo;


    private ColumnSelector columnSelector;

    //private ArrayList<ColumnDetails> columnList = new ArrayList<ColumnDetails>();
    private RecordDefinition recordDef = new RecordDefinition();


    FocusListener focusListner = new FocusAdapter() {

		/* (non-Javadoc)
		 * @see java.awt.event.FocusAdapter#focusLost(java.awt.event.FocusEvent)
		 */
		@Override
		public void focusLost(FocusEvent e) {
			super.focusLost(e);

			setSelectedFieldOnTable();
		}

    };

    /**
     * Panel1 File Details
     *
     */
    public Pnl3RecordType(AbsRowList typeList, JTextComponent message) {
        super();

        columnSelector = new ColumnSelector(message);

        typeCombo = new TreeCombo(BuildTypeComboList.getList(typeList));

		String formDescription
		    = LangConversion.convertId(LangConversion.ST_MESSAGE, "FileWizard_3",
		    		  "This screen will display the first 60 lines of the file. "
		    		+ "<br>Indicate the <i>start</i> of the <b>Record-Type field</b> by clicking on the starting column"
		    		+ "<br>Then click on the start of the Next Field."
		    		+ "<br>To remove a position click on it again.");
		tips = new JEditorPane("text/html", formDescription);

		this.setHelpURLre(Common.formatHelpURL(Common.HELP_WIZARD_RECORD_TYPE));

		this.addComponentRE(1, 5, TIP_HEIGHT, BasePanel.GAP0,
		        BasePanel.FULL, BasePanel.FULL,
				tips);
		//this.setGap(BasePanel.GAP1);
		this.addLineRE("Name", nameTxt);
		this.addLineRE("Field Start", startTxt);
		this.addLineRE("Field Length", lengthTxt);
		this.addLineRE("Type", typeCombo);
		this.setGapRE(BasePanel.GAP0);

		this.addLineRE("Show Hex", columnSelector.hexChk);
		this.setGapRE(BasePanel.GAP0);
		this.addComponentRE(1, 5, FILE_HEIGHT, BasePanel.GAP1,
		        BasePanel.FULL, BasePanel.FULL,
				columnSelector.fileTbl);

		startTxt.addFocusListener(focusListner);
		lengthTxt.addFocusListener(focusListner);

		columnSelector.addMouseListner(new MouseAdapter() {
			public void mousePressed(MouseEvent m) {
			    int col = columnSelector.fileTbl.columnAtPoint(m.getPoint());
			    columnSelector.columnSelected(col);
			    checkSelectedFieldOnTable();
			}
		});
    }

    private void checkSelectedFieldOnTable() {

     	if (recordDef.columnDtls.size() == 1) {
    		setRecordTypeDetails(1, recordDef.columnDtls.get(0).start);
    	} else if (recordDef.columnDtls.size() == 2) {
    		setRecordTypeDetails(recordDef.columnDtls.get(0).start, recordDef.columnDtls.get(1).start);
    	} else if (recordDef.columnDtls.size() > 2) {
    		setRecordTypeDetails(recordDef.columnDtls.get(1).start, recordDef.columnDtls.get(2).start);
    	}
    }

    private void setSelectedFieldOnTable() {

    	try {
    		int start = Integer.parseInt(startTxt.getText());
    		int length = Integer.parseInt(lengthTxt.getText());

    		if (start >= 1 && length >= 1) {
    			recordDef.columnDtls.clear();
    			if (start > 1) {
    				recordDef.columnDtls.add(
    						new ColumnDetails(start,
    								columnSelector.getCurrentDetails().defaultType.intValue()));
    			}
				recordDef.columnDtls.add(
						new ColumnDetails(start + length,
								columnSelector.getCurrentDetails().defaultType.intValue()));

				columnSelector.setColorIndicator();
    		};

    	} catch (Exception e) {
			// TODO: handle exception
		}
    }

    private void setRecordTypeDetails(int start, int pos2) {

    	startTxt.setText(Integer.toString(start));
    	lengthTxt.setText(Integer.toString(pos2 - start));
    }

    /**
     * @see net.sf.RecordEditor.layoutWizard.WizardPanel#getValues(net.sf.RecordEditor.layoutWizard.LayoutWizard.Details)
     */
    public Details getValues() throws Exception {
    	Details ret = columnSelector.getCurrentDetails();
    	KeyField k = ret.getMainKey();
    	k.keyName = nameTxt.getText();
    	k.keyStart = getInteger(startTxt);
    	k.keyLength = getInteger(lengthTxt);
    	k.keyType =  typeCombo.getSelectedItem().key;

    	return ret;
    }

    private int getInteger(JTextField fld)  throws Exception {

    	try {
    		return Integer.parseInt(fld.getText());
    	} catch (Exception e) {
			fld.requestFocus();
			throw e;
		}
    }


    /**
     * @see net.sf.RecordEditor.layoutWizard.WizardPanel#setValues(net.sf.RecordEditor.layoutWizard.LayoutWizard.Details)
     */
    public final void setValues(Details detail) throws Exception {
    	KeyField k = detail.getMainKey();
        columnSelector.readFile(detail, recordDef);
        columnSelector.setValues(detail, recordDef, false);

        nameTxt.setText(k.keyName);
        startTxt.setText(Integer.toString(k.keyStart));
        lengthTxt.setText(Integer.toString(k.keyLength));
        typeCombo.setSelectedKey(k.keyType);
    }
}
