/**
 *
 */
package net.sf.RecordEditor.edit.display.SaveAs;

import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JSplitPane;

import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.JRecord.External.Def.ExternalField;
import net.sf.JRecord.Types.Type;
import net.sf.RecordEditor.edit.util.StandardLayouts;
import net.sf.RecordEditor.re.fileWriter.FixedWriter;
import net.sf.RecordEditor.re.openFile.RecentFiles;
import net.sf.RecordEditor.utils.swing.BasePanel;

/**
 * @author Bruce Martin
 *
 */
public class SaveAsPnlFixed extends SaveAsPnlBase {

	private FixedWriter writer;


	/**
	 * @param commonSaveAsFields common screen fields
	 */
	public SaveAsPnlFixed(CommonSaveAsFields commonSaveAsFields) {
		super(commonSaveAsFields, ".txt", CommonSaveAsFields.FMT_FIXED, RecentFiles.RF_NONE, null, true);

		BasePanel pnl1 = new BasePanel();
		BasePanel pnl2 = new BasePanel();
//		charsetTxt.setMaximumSize(new Dimension(15 * SwingUtils.CHAR_FIELD_WIDTH, charsetTxt.getMinimumSize().height));
//		charsetCombo.setPreferredSize(new Dimension(6 * SwingUtils.CHAR_FIELD_WIDTH, charsetCombo.getPreferredSize().height));

		pnl1.addLineRE("names on first line", namesFirstLine);
		pnl1.addLineRE("space between fields", spaceBetweenFields);
		pnl1.addLineRE("Charset", charsetCombo);

		pnl2.setGapRE(3);
		pnl2.addComponentRE(1, 5, BasePanel.PREFERRED, 1, BasePanel.FULL, BasePanel.FULL,  getSelectBtnPnl());
		pnl2.addComponentRE(1, 5, 130, BasePanel.GAP,
		        BasePanel.FULL, BasePanel.FULL, fieldTbl);
		pnl2.setComponentName(fieldTbl, "FixedColNames");


		panel.addComponentRE(1, 5, BasePanel.FILL, BasePanel.GAP,
		        BasePanel.FULL, BasePanel.FULL,
		        new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, pnl1, pnl2));

		setupPrintDetails(true);
	}

	public void save(String selection, OutputStream outFile) throws IOException, RecordException {
        String fieldSeperator = "";
        String fontname = getCharset();

        if (spaceBetweenFields.isSelected()) {
        	fieldSeperator = " ";
        }


        writer = new FixedWriter(outFile, fieldSeperator, fontname,
        					getFieldLengths(),
        					getIncludeFields());

        save_writeFile(writer, selection);
	}

	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.edit.display.SaveAs.SaveAsPnlBase#getEditLayout()
	 */
	@Override
	public AbstractLayoutDetails getEditLayout(String ext) {
    	AbstractLayoutDetails ret = null;

    	if (commonSaveAsFields.printRecordDetails != null) {
        	List<ExternalField> ef = new ArrayList<ExternalField>(commonSaveAsFields.printRecordDetails.getFieldCount());
	    	int pos = 1;
	    	int sepLength = 0;
	    	List<String> colNames = commonSaveAsFields.flatFileWriter.getColumnNames();
	    	int levels = commonSaveAsFields.flatFileWriter.getLevelCount();
	    	int[] lengths = writer.getColumnWidths();
        	if (spaceBetweenFields.isSelected()) {
        		sepLength = 1;
            }

	    	//TODO  Fix
        	//TODO  Fix
        	//TODO  Fix

        	for (int i = 0; i < levels; i++) {
    			ef.add(new ExternalField(
    					pos, lengths[i],
    					colNames.get(i),
    					"", Type.ftChar, 0, 0, "", "", "", 0));
    			pos += sepLength + lengths[i];
	    	}
        	for (int i = levels; i < colNames.size(); i++) {
	    	//for (int i = 0; i < fieldCount; i++) {
//	    		if (include == null || (include.length > i-levels && include[i-levels])) {
	    			ef.add(new ExternalField(
	    					pos, lengths[i],
	    					colNames.get(i),
	    					"", Type.ftChar, 0, 0, "", "", "", 0));
	    			pos += sepLength + lengths[i];
//	    		}
	    	}

	    	ret = StandardLayouts.getInstance().getFixedLayout(ef, charsetCombo.getText());
    	}
    	return ret;
    }


}
