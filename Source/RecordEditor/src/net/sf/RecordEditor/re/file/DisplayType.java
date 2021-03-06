package net.sf.RecordEditor.re.file;

import net.sf.JRecord.Details.AbstractLayoutDetails;

public class DisplayType {
	public static final int NORMAL = 0;
	public static final int PREFFERED = 1;
	public static final int FULL_LINE = 2;
	public static final int HEX_LINE = 3;
	
    //private static final  int PREFERRED_INC = 0;
    private static final  int FULL_LINE_INC = 1;

	
	public static int displayType(AbstractLayoutDetails layout, int idx) {
		int ret = NORMAL;
		if (idx == layout.getRecordCount()) {
			ret = PREFFERED;
		} else if (idx == layout.getRecordCount() + FULL_LINE_INC) {
			ret = FULL_LINE;
		} else if (idx > layout.getRecordCount() + FULL_LINE_INC) {
			ret = HEX_LINE;
		}
		
		return ret;
	}
	
	public static int displayTypePrint(AbstractLayoutDetails layout, int idx) {
		int ret = NORMAL;
		if (idx == layout.getRecordCount() || isTreeStructure(layout)) {
			ret = PREFFERED;
		} else if (idx == layout.getRecordCount() + FULL_LINE_INC) {
			ret = FULL_LINE;
		} else if (idx > layout.getRecordCount() + FULL_LINE_INC) {
			ret = HEX_LINE;
		}
		
		return ret;
	}
	public static int getFieldCount(AbstractLayoutDetails layout, int idx) {
		int ret = layout.getRecord(idx).getFieldCount();
		if (isTreeStructure(layout)) {
			ret = getMaxFields(layout);
		}
		
		return ret;
	}
	
	public static boolean isTreeStructure(AbstractLayoutDetails layout) {
		return (layout.isXml() || layout.hasChildren());
	}
	
	public static int getMaxFields(AbstractLayoutDetails layout) {
		return layout.getRecord(DisplayType.getRecordMaxFields(layout)).getFieldCount();
	}
	
	public static int getRecordMaxFields(AbstractLayoutDetails layout) {
		int idx = 0;
		int fields = -1;
		
		for (int i = 0; i < layout.getRecordCount(); i++) {
			if (fields < layout.getRecord(i).getFieldCount()) {
				idx = i;
				fields = layout.getRecord(i).getFieldCount();
			}
		}
		return idx;
	}
}
