package net.sf.RecordEditor.edit.display.SaveAs;

import java.awt.event.FocusListener;

import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JTextArea;

import net.sf.JRecord.Details.AbstractRecordDetail;
import net.sf.RecordEditor.re.display.AbstractFileDisplay;
import net.sf.RecordEditor.re.file.AbstractTreeFrame;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.lang.LangConversion;

public final class CommonSaveAsFields {
    public static final String OPT_FILE = LangConversion.convertComboItms("File SelectionOptions", "File");
    public static final String OPT_VIEW = LangConversion.convertComboItms("File SelectionOptions", "Current View");
    public static final String OPT_SELECTED = LangConversion.convertComboItms("File SelectionOptions", "Selected Records");


	public final static int FMT_DATA = 0;
	public final static int FMT_CSV = 1;
	public final static int FMT_FIXED = 2;
	public final static int FMT_XML = 3;
	public final static int FMT_HTML = 4;
	public final static int FMT_SCRIPT = 5;
	public final static int FMT_XSLT = 6;
	public final static int FMT_VELOCITY = 7;
	public final static int FMT_FILE_STRUCTURE = 8;

    public final JComboBox saveWhat   = new JComboBox();

    public final JCheckBox treeExportChk    = new JCheckBox(),
    		               nodesWithDataChk = new JCheckBox(),
    		               keepOpenChk      = new JCheckBox(),
    		               editChk          = new JCheckBox();

    public final JTextArea message = new JTextArea();

    public final FileView file;
    public final SaveAsWrite flatFileWriter;
    public final FocusListener templateListner;

    private final AbstractFileDisplay recordFrame;
    @SuppressWarnings("rawtypes")
	private AbstractTreeFrame treeFrame = null;

    protected AbstractRecordDetail printRecordDetails;





	/**
	 * @return the recordFrame
	 */
	protected AbstractFileDisplay getRecordFrame() {
		return recordFrame;
	}


	/**
	 * @param recordFrame the recordFrame to set
	 */
	public CommonSaveAsFields(
			final AbstractFileDisplay recordFrame, final FileView file, final FocusListener templateListner) {
		this.recordFrame = recordFrame;
		this.file = file;
		this.templateListner = templateListner;

		int[] selected = recordFrame.getSelectedRows();

		treeFrame = null;
        if (recordFrame instanceof AbstractTreeFrame) {
        	treeFrame = (AbstractTreeFrame) recordFrame;
        }
        flatFileWriter = SaveAsWrite.getWriter(file, getRecordFrame());

       if (file.isView()) {
            saveWhat.addItem(OPT_VIEW);
        }
        saveWhat.addItem(OPT_FILE);

        if (selected != null && selected.length > 0) {
        	saveWhat.addItem(OPT_SELECTED);
        }
	}


	/**
	 * @return the treeFrame
	 */
	@SuppressWarnings("rawtypes")
	protected AbstractTreeFrame getTreeFrame() {
		return treeFrame;
	}


    public final int getWhatToSave(String selection) {
        int whatToSave = SaveAsWrite.SAVE_SELECTED;
        if (OPT_FILE.equals(selection)) {
        	whatToSave = SaveAsWrite.SAVE_FILE;
        } else if (OPT_VIEW.equals(selection)) {
        	whatToSave = SaveAsWrite.SAVE_VIEW;
        }
        return whatToSave;
    }


	public final FileView getViewToSave(String selection) {
    	return getViewToSave(getWhatToSave(selection));
    }


	public final FileView getViewToSave(int whatToSave) {
    	FileView ret = null;
    	switch (whatToSave) {
    	case SaveAsWrite.SAVE_SELECTED: ret = file.getView(recordFrame.getSelectedRows()); break;
    	case SaveAsWrite.SAVE_FILE: ret = file.getBaseFile();							   break;
    	case SaveAsWrite.SAVE_VIEW: ret = file;
    	}

    	return ret;
   	}

    public final void setVisibility(int pnlFormat, boolean singleTable) {

    	boolean visible = (   pnlFormat == FMT_CSV
    					   || pnlFormat == FMT_FIXED
    					   || (   pnlFormat == FMT_HTML
    					      &&  singleTable)
    					   || (   pnlFormat == FMT_XML
    					      &&  getTreeFrame() != null)
    					  )
    			       && (       saveWhat.getItemCount() == 1
    			           ||     OPT_VIEW.equals(saveWhat.getSelectedItem())
    			           || (   OPT_FILE.equals(saveWhat.getSelectedItem())
    			         	  &&  ! file.isView())
    			           );

    	treeExportChk.setVisible(visible);
    	nodesWithDataChk.setVisible(visible &&  pnlFormat != FMT_XML);
    }
}
