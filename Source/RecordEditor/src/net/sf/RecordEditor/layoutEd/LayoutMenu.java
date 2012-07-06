/*
 * @Author Bruce Martin
 * Created on 10/01/2007
 *
 * Purpose:
 * Top level dropdown menu with basic layout functions
 *
 * Changes
 * * Version 0.61
 *   - Set the callback in the create (layout) action in the
 *     setDatabaseDetails (fixes bug of create Layout menu not working
 *     in the full editor
 *   - Added try { } catch blocks around addSeperator calls to
 *     support more LookAndFeel packages
 *
 */
package net.sf.RecordEditor.layoutEd;

import java.awt.event.ActionEvent;

import net.sf.RecordEditor.layoutEd.Record.SaveLayoutsDBAsXml;
import net.sf.RecordEditor.layoutEd.panels.LoadCobolIntoDBScreen;
import net.sf.RecordEditor.layoutEd.panels.RecordEdit1Record;
import net.sf.RecordEditor.layoutWizard.Wizard;
import net.sf.RecordEditor.re.util.LoadXmlLayoutsIntoDB;
import net.sf.RecordEditor.utils.LayoutConnection;
import net.sf.RecordEditor.utils.LayoutConnectionAction;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.ReAbstractAction;
import net.sf.RecordEditor.utils.lang.ReMenu;


/**
 *
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class LayoutMenu extends ReMenu {

    private static final int SYSTEM_TABLE = 3;
    private LayoutConnection databaseDetails;
    private LayoutConnectionAction create;
    private LayoutConnectionAction createWizard;


    /**
     * Layout menu
     * @param dbDetails Current Database details (callback)
     */
    public LayoutMenu(final LayoutConnection dbDetails) {
        super("Record Layouts");

        databaseDetails = dbDetails;

        ReAbstractAction edit = new ReAbstractAction(
        		"Edit Layout",
        		Common.getRecordIcon(Common.ID_LAYOUT_EDIT_ICON)) {
            public void actionPerformed(ActionEvent e) {
                new RecordEdit(databaseDetails.getCurrentDbName(),
                               databaseDetails.getCurrentDbIdentifier());
            }
        };
        createWizard = Wizard.getAction(databaseDetails);
        ReAbstractAction editSystemTable = new ReAbstractAction(
        		"Edit System Table") {
            public void actionPerformed(ActionEvent e) {
                new TblEdit(databaseDetails.getCurrentDbName(),
                        null,
                        databaseDetails.getCurrentDbIdentifier(),
                        SYSTEM_TABLE);
            }
        };
        ReAbstractAction comboEdit = new ReAbstractAction(
        		"Edit Combo Lists",
        		Common.getRecordIcon(Common.ID_COMBO_EDIT_ICON)) {
            public void actionPerformed(ActionEvent e) {
            	new ComboEdit(
            			databaseDetails.getCurrentDbName(),
        				databaseDetails.getCurrentDbIdentifier());
            }
        };

        ReAbstractAction loadCobol = new ReAbstractAction("Load Cobol Copybook") {
            public void actionPerformed(ActionEvent e) {
		        new LoadCopyBook(
        				false,
        						/* choosing between Cobol and XML Copybooks */
        				databaseDetails.getCurrentDbName(),
        				databaseDetails.getCurrentDbIdentifier(),
        				databaseDetails);
            }
        };
        ReAbstractAction loadCopybook = new ReAbstractAction("Load Copybook") {
            public void actionPerformed(ActionEvent e) {
		        new LoadCopyBook(
        				true,
        						/* choosing between Cobol and XML Copybooks */
        				databaseDetails.getCurrentDbName(),
        				databaseDetails.getCurrentDbIdentifier(),
        				databaseDetails);
            }
        };
        ReAbstractAction saveCopybooksAsXml = new ReAbstractAction("Save Copybooks as Xml") {
            public void actionPerformed(ActionEvent e) {
		        new SaveLayoutsDBAsXml(databaseDetails.getCurrentDbIdentifier());
            }
        };
        ReAbstractAction loadCopybooksFromXml = new ReAbstractAction("Load Copybooks from Xml") {
            public void actionPerformed(ActionEvent e) {
		        new LoadXmlLayoutsIntoDB(databaseDetails.getCurrentDbIdentifier());
            }
        };
        ReAbstractAction loadCopybooksFromCobol = new ReAbstractAction("Load Copybooks from Cobol Directory") {
            public void actionPerformed(ActionEvent e) {
		        new LoadCobolIntoDBScreen(databaseDetails.getCurrentDbIdentifier());
            }
        };


        create = RecordEdit1Record.getAction(databaseDetails);

        this.add(edit);
        this.add(create);
        this.add(createWizard);

        addSeperator();

        this.add(comboEdit);

        addSeperator();

        this.add(loadCobol);
        this.add(loadCopybook);
        this.add(saveCopybooksAsXml);
        this.add(loadCopybooksFromXml);
        this.add(loadCopybooksFromCobol);

        addSeperator();

        this.add(editSystemTable);
    }

    private void addSeperator() {

        try {
            this.addSeparator();
        } catch (Exception e) {
        }
    }


    /**
     * Set the DB connection class
     * @param dbDetails The databaseDetails to set.
     */
    public void setDatabaseDetails(LayoutConnection dbDetails) {
        this.databaseDetails = dbDetails;
        create.setCallback(dbDetails);
        createWizard.setCallback(dbDetails);
    }
}
