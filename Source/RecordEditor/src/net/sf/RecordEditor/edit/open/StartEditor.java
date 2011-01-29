package net.sf.RecordEditor.edit.open;

import javax.swing.JTextArea;
import javax.swing.SwingWorker;

import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.RecordEditor.edit.display.BaseDisplay;
import net.sf.RecordEditor.edit.display.LineList;
import net.sf.RecordEditor.edit.display.LineTree;
import net.sf.RecordEditor.edit.display.LineTreeChild;
import net.sf.RecordEditor.edit.file.FileView;
import net.sf.RecordEditor.edit.tree.LineNodeChild;
import net.sf.RecordEditor.edit.tree.TreeParserXml;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.swing.EditingCancelled;

public class StartEditor extends SwingWorker<Void, Void> {
	protected FileView<?> file;
	protected String fName;
	private boolean pBrowse;
	
	protected boolean ok = false;
	private JTextArea   message;
	private int initialRow;
	//RecentFilesList recentList;


	public StartEditor(FileView<?> file, 
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
			execute();
		} else {
			doInBackground();
			done();
		}
	}

	@Override
	public Void doInBackground() {
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
			message.setText(e.getMessage());
		} catch (Exception e) {
			message.setText("Error Reading the File: " + e.getMessage());
			Common.logMsg(e.getMessage(), e);
			e.printStackTrace();
		}
		return null;
	}

 
	@Override
	public void done() {
		
		if (ok) {
			doOpen(file, initialRow, pBrowse);
			
			message.setText(file.getMsg());
		}
	}
	
	public static void doOpen(FileView<?> file, int initialRow, boolean pBrowse) {
		
		BaseDisplay display = null;
		AbstractLayoutDetails<?,?> layoutDtls = file.getLayout();

		if (layoutDtls.hasChildren()) {
			display = new LineTreeChild(file, new LineNodeChild("File", file), true, 0);
			if (file.getRowCount() == 0 && ! pBrowse) {
				display.insertLine(0);
			}
		} else if (layoutDtls.isXml()) {
			display = new LineTree(file, TreeParserXml.getInstance(), true, 1);
		} else {
			display = new LineList(layoutDtls, file, file);
			display.setCurrRow(initialRow, -1, -1);

			if (file.getRowCount() == 0 && ! pBrowse) {
				display.insertLine(0);
			}
		}		
	}
}
