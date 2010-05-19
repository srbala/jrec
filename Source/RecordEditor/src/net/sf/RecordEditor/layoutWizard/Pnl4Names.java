/*
 * @Author Bruce Martin
 * Created on 8/01/2007
 *
 * Purpose:
 * 3rd and final wizard panel where the user enters field
 * details
 *
 * Changes
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Name changes, remove done method call
 *
 * # Version 0.61b Bruce Martin 2007/05/05
 *  - Changes o support user selecting the default type
 */
package net.sf.RecordEditor.layoutWizard;

import javax.swing.JEditorPane;
import javax.swing.JScrollPane;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.swing.AbsRowList;
import net.sf.RecordEditor.utils.swing.BasePanel;


/**
 * 3rd and final wizard panel where the user enters field
 * details
 *
 * @author Bruce Martin
 *
 */
public class Pnl4Names extends WizardPanel {

    private static final int COLUMN_HEIGHT  = 150;
    private static final int FILE_HEIGHT = 130;

    private ColumnNames columnNames;
    /**
     * Panel1 File Details
     *
     * @param connectionIdx Conection Identifier
     */
    public Pnl4Names(AbsRowList typeList) {
        super();

		String formDescription
		    = "This screen will display the Column Details and allow you to change them. ";
		JEditorPane tips = new JEditorPane("text/html", formDescription);
		
		columnNames = new ColumnNames(typeList);


		this.setHelpURL(Common.formatHelpURL(Common.HELP_WIZARD_PNL3));
		this.addComponent(1, 5, TIP_HEIGHT, BasePanel.GAP3,
		        BasePanel.FULL, BasePanel.FULL,
				new JScrollPane(tips));
		this.setGap(BasePanel.GAP1);
		this.addComponent(1, 5, COLUMN_HEIGHT, BasePanel.GAP1,
		        BasePanel.FULL, BasePanel.FULL,
				new JScrollPane(columnNames.columnTbl));
		this.addComponent(1, 5, FILE_HEIGHT, BasePanel.GAP0,
		        BasePanel.FULL, BasePanel.FULL,
				new JScrollPane(columnNames.fileTbl));
    }




    /**
     * @see net.sf.RecordEditor.layoutWizard.WizardPanel#getValues(net.sf.RecordEditor.LayoutWizard.Details)
     */
    public Details getValues() throws Exception {
       
        return columnNames.getValues();
    }

    /**
     * @see net.sf.RecordEditor.layoutWizard.WizardPanel#setValues(net.sf.RecordEditor.LayoutWizard.Details)
     */
    public void setValues(Details detail) throws Exception {

    	columnNames.setValues(detail, detail.standardRecord);
     }
}
