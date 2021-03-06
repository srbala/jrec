package net.sf.RecordEditor.edit.open;

import javax.swing.JTextArea;

import net.sf.RecordEditor.re.display.AbstractFileDisplayWithFieldHide;
import net.sf.RecordEditor.re.display.DisplayBuilderFactory;
import net.sf.RecordEditor.re.display.IDisplayBuilder;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.GcManager;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.swing.EditingCancelled;

public class StartEditor {
	protected FileView file;
	protected String fName;
	private boolean pBrowse;

	protected boolean ok = false;
	private JTextArea   message;
	private int initialRow;
	
	public AbstractFileDisplayWithFieldHide screen;
	//RecentFilesList recentList;


	public StartEditor(FileView file,
			String name, boolean browse,
			JTextArea   messageFld,
			int startRow) {
		super();
		this.file = file;
		fName = name;
		pBrowse = browse;
		message = messageFld;
		initialRow = startRow;
	}

	public void doEdit() {
		if (Common.OPTIONS.loadInBackgroundThread.isSelected()) {
			try {
				GcManager.doGcIfNeccessary(0.5);
				(new net.sf.RecordEditor.edit.open.StartEditorBackGround(this)).execute();
				return;
			} catch (NoClassDefFoundError e) {
			}
		}
		doRead();
		done();

	}
	public void doRead() {
		try {
			file.readFile(fName);
			ok = true;
//		} catch (IOException e) {
//			message.setText("Error Reading the File: " + e.getMessage());
//			Common.logMsg(e.getMessage(), e);
//		} catch (RecordException e) {
//			message.setText("Error Reading the File: " + e.getMessage());
//			Common.logMsg(e.getMessage(), e);
		} catch (EditingCancelled e) {
			if (message == null) {
				Common.logMsgRaw(e.getMessage(), null);
			} else {
				message.setText(e.getMessage());
			}
		} catch (Exception e) {
			if (message != null) {
				message.setText(LangConversion.convert("Error Reading the File:") + " " + e.toString());
			}
			Common.logMsgRaw(e.getMessage(), e);
			e.printStackTrace();
		}
	}


	public void done() {

		if (ok) {
			int opt = IDisplayBuilder.ST_INITIAL_EDIT;
			if (pBrowse) {
				opt = IDisplayBuilder.ST_INITIAL_BROWSE;
			}
			//DisplayBuilder.doOpen(file, initialRow, pBrowse);
			screen = DisplayBuilderFactory.getInstance().newDisplay(opt, "", null, file.getLayout(), file, initialRow);

			if (message != null) {
				message.setText(file.getMsg());
			}
		}
	}
}
