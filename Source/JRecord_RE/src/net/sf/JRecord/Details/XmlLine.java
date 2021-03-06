/*
 * @Author Bruce Martin
 * Created on 20/04/2007
 *
 * Purpose:
 */
/*  -------------------------------------------------------------------------
 *
 *            Sub-Project: RecordEditor's version of JRecord 
 *    
 *    Sub-Project purpose: Low-level IO and record translation  
 *                        code + Cobol Copybook Translation
 *    
 *                 Author: Bruce Martin
 *    
 *                License: GPL 2.1 or later
 *                
 *    Copyright (c) 2016, Bruce Martin, All Rights Reserved.
 *   
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU General Public License
 *    as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *   
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 * ------------------------------------------------------------------------ */
      
package net.sf.JRecord.Details;

import net.sf.JRecord.Common.FieldDetail;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Common.XmlConstants;

/**
 * Line that represent one Xml-Tag in a XML file.
 *
 * <p>The one important method is getFieldValue
 *
 * <p>Creating:
 * <pre>
 *              AbstractLine outLine = <font color="brown"><b>new</b></font> XmlLine(oLayout, recordIdx);
 * </pre>
 *
 * <p>Getting a field value:
 * <pre>
 *              <font color="brown"><b>long</b></font> sku = saleRecord.getFieldValue("<font color="blue"><b>KEYCODE-NO</b></font>").asLong();
 * </pre>
 *
 * <p>Updating a field:
 * <pre>
 *              saleRecord.getFieldValue("<font color="blue"><b>KEYCODE-NO</b></font>").set(1331);
 * </pre>
 *
 * @author Bruce Martin
 *
 */
public class XmlLine extends ArrayListLine<FieldDetail, RecordDetail, LayoutDetail> {
	private boolean useField4Index = true;

    public XmlLine(LayoutDetail layoutDetails, int recordIdx) {
	    super(layoutDetails, recordIdx, 0);
	}


	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getField(int, int)
	 */
    public Object getField(int recordIdx, int fieldIdx) {
    	int idx = getFieldNumber(recordIdx, fieldIdx);

    	if (fields.size() > idx && idx >= 0) {
    		return fields.get(idx);
    	}

    	return null;
    }

    /**
     * Get a fields value
     *
     * @param fieldName field to retrieve
     *
     * @return fields Value
     *
     * @deprecated use getFieldValue
     */
	public Object getField(String fieldName) {
	    try {
	    	return getField(preferredLayout,
	    			layout.getRecord(preferredLayout).getFieldIndex(fieldName));
	    } catch (Exception e) {
			return null;
		}
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getField(net.sf.JRecord.Common.FieldDetail)
	 */
	public Object getField(FieldDetail field) {
		//super.getField(field)
		if (field == null) return null;
	    return getFieldRaw(preferredLayout, field.getPos());
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setField(int, int, java.lang.Object)
	 */
	public void setField(int recordIdx, int fieldIdx, Object val)
			throws RecordException {
				setRawField(recordIdx, getFieldNumber(recordIdx, fieldIdx), val);
	}

	private int getFieldNumber(int recordIdx, int fieldIdx) {
	   	int idx = fieldIdx;

		if (useField4Index && recordIdx < layout.getRecordCount()
       	&& fieldIdx < layout.getRecord(recordIdx).getFieldCount()
       	&& fieldIdx >= 0
       	&& layout.getRecord(recordIdx).getField(fieldIdx).getPos() >= 0) {
       		idx = layout.getRecord(recordIdx).getField(fieldIdx).getPos();
       	}
//	     	System.out.println("getField " + recordIdx + " " + fieldIdx + " " + idx);
   	return idx;
	}

	/**
	 * @param useField4Index the useField4Index to set
	 */
	public final void setUseField4Index(boolean useField4Index) {
		this.useField4Index = useField4Index;
	}

	public void setRawField(int recordIdx, int fieldIdx, Object val)
	throws RecordException {

		super.setRawField(recordIdx, fieldIdx, val);

        if (val != null || fields.get(fieldIdx) != null) {
        	rebuildRequired = (fieldIdx == 0) || (fieldIdx == XmlConstants.END_INDEX) || newRecord;

        	if (val != null && fieldIdx == XmlConstants.NAME_INDEX) {
        		int idx = layout.getRecordIndex(val.toString());
        		if (idx >= 0) {
        			preferredLayout = idx;
        		}
        	}
        }
    }


	/* (non-Javadoc)
	 * @see net.sf.JRecord.Details.ArrayListLine#clone()
	 */
	@Override
	public Object clone() {
        Object ret = null;

        try { ret = super.clone(); } catch (Exception e) {}

        if (! (ret instanceof ArrayListLine)) {
        	XmlLine line = new XmlLine(layout, preferredLayout);
        	for (int i = 0; i < fields.size(); i++) {

        		try {
        			line.setRawField(preferredLayout, i, fields.get(i));
        		} catch (Exception e) {
				}
        	}
        	ret = line;
        }
        return ret;
	}

}
