/*
 * Created on 25/08/2004
 *
 * Changes
 * # Version 0.56 Bruce Martin 2007/01/16
 *   - changed to use ReFrame (from JInternalFrame) which keeps track
 *     of the active form
 *   - changed to use ReActionHandler instead of ActionListener
 *
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Bug fix, JRecord
 */
package net.sf.RecordEditor.layoutEd;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JSplitPane;
import javax.swing.JTextField;
import javax.swing.event.InternalFrameAdapter;
import javax.swing.event.InternalFrameEvent;

import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.JRecord.Details.IGetSchema;
import net.sf.RecordEditor.layoutEd.Record.SearchArgAction;
import net.sf.RecordEditor.layoutEd.panels.RecordListPnl;
import net.sf.RecordEditor.layoutEd.panels.RecordPnl;
import net.sf.RecordEditor.layoutEd.utils.LeMessages;
import net.sf.RecordEditor.re.db.Record.ExtendedRecordDB;
import net.sf.RecordEditor.re.db.Record.RecordRec;
import net.sf.RecordEditor.re.db.Record.SaveRecordAsXml;
import net.sf.RecordEditor.utils.BasicLayoutCallback;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.common.ReActionHandlerWithSave;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.lang.ReOptionDialog;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.screenManager.ReMainFrame;
import net.sf.RecordEditor.utils.swing.SwingUtils;





/**
 * This class display containing:
 * <ul compact>
 * <li>A pane where the user can select various record layouts
 * <li>A pane where a record layout is updated
 * </ul>
 *
 * @author Bruce Martin
 * @version 0.51
 */
@SuppressWarnings("serial")
public class RecordEdit extends    ReFrame
						implements SearchArgAction, ReActionHandlerWithSave, BasicLayoutCallback,
						           IGetSchema{

    private static final int MAIN_PANEL_HEIGHT_ADJUSTMET =  SwingUtils.STANDARD_FONT_HEIGHT * 5;
 	private RecordListPnl pnlRecordList;

	private RecordPnl pnlRecord;

	//private JSplitPane splitPane;

	private JTextField message     = new JTextField(" ");

	private int currRow = 0;
	private int connectionIdx;

	private ReMainFrame frame;

	private ReActionHandler recordActionHandler = null;



	/**
	 * Edit the Record Layouts
	 *
	 * @param dbName Current Database Index
	 * @param dbConnectionIdx  Database Connection Index
	 */
	public RecordEdit(final String dbName,
	        		  final int dbConnectionIdx)   {
		super(dbName, "Edit Record Layout - DB", null); //iconifiable

		frame = ReMainFrame.getMasterFrame();
		int height = frame.getDesktop().getHeight() - 1;
		int width  = frame.getDesktop().getWidth() - 1;
		boolean free = Common.isSetDoFree(false);

		this.connectionIdx = dbConnectionIdx;

		Container cont = getContentPane();
		cont.setLayout(new BorderLayout());

		defLeftPnl();
		defRightPanel();

		JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT,
								   pnlRecordList,
								   pnlRecord);

		message.setEditable(false);
		message.setText(Common.getJdbcMsg(dbConnectionIdx));

		cont.add(BorderLayout.NORTH, splitPane);
		cont.add(BorderLayout.SOUTH, message);
		splitPane.setPreferredSize(
		        new Dimension(width, height - message.getHeight() - MAIN_PANEL_HEIGHT_ADJUSTMET));

		pack();

		this.setBounds(1, 1, width, height);

		this.addInternalFrameListener(new InternalFrameAdapter() {
			public void internalFrameClosed(final InternalFrameEvent e) {
				saveRecord(! Common.TEST_MODE);
				Common.checkpoint(connectionIdx);
			}
		});

		show();
		Common.setDoFree(free, dbConnectionIdx);
	}


	/**
	 * Define the left panel
	 *
	 */
	public void defLeftPnl() {

		pnlRecord = new RecordPnl(frame, connectionIdx, this, true, false);
		pnlRecordList = new RecordListPnl(frame, connectionIdx, pnlRecord, this);
		pnlRecordList.addMouseListener(new MouseAdapter() {
			public void mousePressed(final MouseEvent m) {
				setRecord(pnlRecordList.getSelectedRow());
			}
		});
		pnlRecordList.addActionListener(this);
		recordActionHandler = pnlRecord.getRecordActionHandler();
	}


	/**
	 * Define the right panel
	 *
	 */
	public void defRightPanel() {

		 //dbTblList,
									 //	(RecRecord) dbRecordModel.getRecord(0));
		pnlRecord.setValues(pnlRecordList.getRecord(0));

//		pnlRecord.setMinimumSize(
//		        new Dimension(RECORD_PANEL_WIDTH,
//		                      RECORD_PANEL_HIEGHT));
	}


	/**
	 * This method changes the row being displayed
	 *
	 * @param row new row to be displayed
	 */
	private void setRecord(final int row) {

		if (currRow != row) {
			boolean free = Common.isSetDoFree(false);
			RecordRec rec = pnlRecord.getValues();

			if (rec.getRecordName() == null || rec.getRecordName().length() == 0) {
				message.setText(LeMessages.NO_RECORD_NAME.get());
			} else 	if (rec != null && rec.isUpdateSuccessful()) {
				pnlRecordList.setRecord(currRow, rec);
				pnlRecord.saveRecordDetails();

				setRecordId(row);
			} else {
				message.setText(pnlRecord.getMsg());
			}
			Common.setDoFree(free, connectionIdx);
		}
	}

	/**
	 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
	 */
	public void searchArgChanged() {
		boolean free = Common.isSetDoFree(false);

		RecordRec rec = saveRecord(true);

		if (rec == null || rec.isUpdateSuccessful()) {
			pnlRecordList.changeSearchArgs();

			setRecordId(0);
		}
		Common.setDoFree(free, connectionIdx);
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.common.ReActionHandlerWithSave#doSave()
	 */
	@Override
	public boolean saveOk() {
		RecordRec rec = saveRecord(true);
		return  rec != null && rec.isUpdateSuccessful();
	}

	/**
	 * save the Record Layout details being displayed to the user
	 *
	 * @return Record Layout just saved
	 */
	public RecordRec saveRecord(boolean requireRecordName) {

		RecordRec rec = pnlRecord.getValues();

		if (rec != null) {
			if (requireRecordName && "".equals(rec.getValue().getRecordName())) {
				message.setText("Record Name is required");
				rec = null;
			} else if (rec.isUpdateSuccessful()) {
				message.setText(pnlRecordList.setRecord(currRow, rec));

				pnlRecord.saveRecordDetails();
			} else {
				message.setText(pnlRecord.getMsg());
			}
		}

		return rec;
	}


	/**
	 * Set the Current Row
	 *
	 * @param row new current row
	 */
	private void setRecordId(int row) {

		currRow = row;
		RecordRec rec =  pnlRecordList.getRecord(row);
		pnlRecord.setValues(rec);

		message.setText("");
	}



	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.screenManager.ReFrame#executeAction(int, java.lang.Object)
	 */
	@Override
	public void executeAction(int action, Object o) {
		if (action == ReActionHandler.EXPORT_VELOCITY) {
			String s = "";
			if (o != null) {
				s = o.toString();
			}

			RecordRec rec1 = saveRecord(true);

			if (rec1 != null) {
				new net.sf.RecordEditor.layoutEd.panels.ExportVelocityPnl(
					connectionIdx, s, ExtendedRecordDB.getRecord(connectionIdx, rec1.getRecordId()));
			} else {
				Common.logMsg("No Layout to Export", null);
			}
		} else {
			executeAction(action);
		}
	}


	/**
	 * Execut the requested action
	 *
	 * @param action action to perform
	 */
	public void executeAction(int action) {

	    String msg = "";

	    switch (action) {
	    case ReActionHandler.HELP:
	        pnlRecord.showHelpRE();
	        break;
	    case ReActionHandler.DELETE:
	        if (pnlRecord.isOkToDelete()) {
	            msg = pnlRecordList.deleteRecord(currRow);

	            if ("".equals("")) {
	                pnlRecord.deleteRecordDetails();
	                pnlRecord.setValues(null);

	                currRow -= 1;
	                if (currRow < 0) {
	                    currRow = 0;
	                }
	                setRecordId(currRow);
	            }
	        }
	        break;
	    case ReActionHandler.SAVE:
	        if (saveRecord(true) == null) {
	        	return;
	        }
	        break;
	    case ReActionHandler.NEW:
	    case ReActionHandler.SAVE_AS:

	        RecordRec rec = saveRecord(false);

	        if (rec != null && rec.isUpdateSuccessful()) {
	            int tRow;
	            if (action == ReActionHandler.NEW) {
	                rec = RecordRec.getNullRecord("", "");
	                rec.getValue().setListChar("Y");

	                tRow = pnlRecordList.addRecord(rec);

	                if (tRow > 0) {
	                    currRow = tRow;
	                    pnlRecord.setValues(rec);
	                }
	            } else if (action == ReActionHandler.SAVE_AS) {
	                String newName = ReOptionDialog.showInputDialog(this, "New Record Layout Name", rec.getRecordName());

	                if (newName != null && ! "".equals(newName)) {
	                    rec = (RecordRec) rec.clone();
	                    rec.getValue().setRecordName(newName);
	                    tRow = pnlRecordList.addRecord(rec);

	                    if (tRow > 0) {
	                        currRow = tRow;
	                        pnlRecord.set2clone(rec);
	                    }
	                    this.message.setText(LangConversion.convert("Old record saved, New Record {0} created", newName));
	                }
	            }
	        }
	        break;
	    case ReActionHandler.SAVE_LAYOUT_XML:
	    	//TODO
	        RecordRec rec1 = saveRecord(true);

	        if (rec1 != null && rec1.isUpdateSuccessful()) {
	        	new SaveRecordAsXml(connectionIdx, rec1.getRecordId());
	        }
	    	break;
	    default:
	        recordActionHandler.executeAction(action);
	    }

	    message.setText(msg);
	}

    /**
     * @see net.sf.RecordEditor.utils.common.ReActionHandler#isActionAvailable(int)
     */
    public boolean isActionAvailable(int action) {

        boolean ret = (action == ReActionHandler.HELP)
    		|| (action == ReActionHandler.DELETE)
        	|| (action == ReActionHandler.SAVE)
            || (action == ReActionHandler.NEW)
            || (action == ReActionHandler.SAVE_LAYOUT_XML)
            || (action == ReActionHandler.EXPORT_VELOCITY)
        	|| (action == ReActionHandler.SAVE_AS);

        if (recordActionHandler != null && ! ret) {
        	ret = recordActionHandler.isActionAvailable(action);
        }
        return ret;
    }


	/* (non-Javadoc)
	 * @see net.sf.JRecord.Details.IGetSchema#getSchema()
	 */
	@Override
	public AbstractLayoutDetails getSchema() {
        RecordRec rec1 = saveRecord(true);

        if (rec1 != null && rec1.isUpdateSuccessful()) {
        	RecordRec recr = ExtendedRecordDB.getRecord(connectionIdx, rec1.getRecordId());
        	if (recr != null) {
        		return recr.getValue().asLayoutDetail();
        	}
        }
		return null;
	}

	

	/* (non-Javadoc)
	 * @see net.sf.JRecord.Details.IGetSchema#schemaAvailable4checking()
	 */
	@Override
	public int schemaChecking() {
		return IGetSchema.ST_NO_CHECK_ON_SCHEMA;
	}



	@Override
	public void setRecordLayout(int layoutId, String layoutName, String filename) {
		searchArgChanged();
	}
    
    
}
