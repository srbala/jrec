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

import java.util.ArrayList;
import java.util.HashMap;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.FieldDetail;
import net.sf.JRecord.Common.IFieldDetail;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Common.XmlConstants;


/**
 * Implementation of a "Line" based on a ArraryList of fields.
 *
 * @author Bruce Martin
 *
 * @param <FieldDef> Field Definition Class
 * @param <RecordDef> Record Definition class
 * @param <Layout> Schema class
 */
public class ArrayListLine<
								FieldDef extends FieldDetail,
								RecordDef extends AbstractRecordDetail,
								Layout extends AbstractLayoutDetails>
extends BaseLine<Layout>
implements AbstractLine {

//	private static final AbstractTreeDetails<FieldDetail, Recor dDetail, LayoutDetail, ArrayListLine, Object>
//				NULL_TREE_DETAILS = new NullTreeDtls<FieldDetail, RecordDetail, LayoutDetail, AbstractChildDetails<RecordDetail>, ArrayListLine, Object>();
	protected ArrayList<Object> fields = new ArrayList<Object>();
	protected int preferredLayout = Constants.NULL_INTEGER;
	protected boolean newRecord;
	protected boolean rebuildRequired = false;
	protected AbstractTreeDetails<FieldDef, RecordDef, Layout, ArrayListLine<FieldDef, RecordDef, Layout>>
						children; // = NULL_TREE_DETAILS;
//NullTreeDtls.STANDCopyOfSimpleLineARD_NULL_DETAILS;
	//children = null;

	private final int fieldStartingPos;

	@SuppressWarnings("rawtypes")
	private static HashMap<Class, AbstractTreeDetails> nullTrees = new HashMap<Class, AbstractTreeDetails>(5);

   public ArrayListLine(Layout layoutDetails, int recordIdx, int fieldStartingPosition) {
	   super(layoutDetails);

	    //layout =layoutDetails;
	    newRecord = recordIdx < 0;
	    preferredLayout = recordIdx;
	    fieldStartingPos = fieldStartingPosition;

	    fields.add("");

	    if (newRecord) {
	    	fields.add("True");
	    }

	    if (layout != null && layout.hasChildren()) {
	    	children = new TreeDetails<FieldDef, RecordDef, Layout, AbstractChildDetails<RecordDef>,
	    												ArrayListLine<FieldDef, RecordDef, Layout>>();
	    	//FieldDetail, RecordDetail, LayoutDetail, AbstractChildDetails<RecordDetail>, ArrayListLine, Object>();
	    } else {
	    	children = getNullTree();
	    }
	}

   private AbstractTreeDetails<FieldDef, RecordDef, Layout, ArrayListLine<FieldDef, RecordDef, Layout>> getNullTree() {
	   AbstractTreeDetails<FieldDef, RecordDef, Layout, ArrayListLine<FieldDef, RecordDef, Layout>> ret;

	   if (nullTrees.containsKey(this.getClass())) {
		   ret = nullTrees.get(this.getClass());
	   } else {
		   ret = new NullTreeDtls<FieldDef, RecordDef, Layout, AbstractChildDetails<RecordDef>, ArrayListLine<FieldDef, RecordDef, Layout>>();
		   nullTrees.put(this.getClass(), ret);
	   }

	   return ret;
   }

	/**
	 * @see java.lang.Object#clone()
	 */
	public Object clone() {
	        Object ret = null;

	        try { ret = super.clone(); } catch (Exception e) {}

	        if (! (ret instanceof ArrayListLine)) {
	        	ArrayListLine<FieldDef, RecordDef, Layout> line
	        			= new ArrayListLine<FieldDef, RecordDef, Layout>(layout, preferredLayout, fieldStartingPos);
	        	for (int i = 0; i < fields.size(); i++) {
	//        		Object o = fields.get(i);
	//        		if (o != null
	//        		&& ! (o instanceof String
	//        		   || o instanceof Boolean
	//        		   || o instanceof BigInteger
	//        		   || o instanceof BigDecimal)) {
	//					   o = o.toString();
	//				}
	        		try {
	        			line.setRawField(preferredLayout, i, fields.get(i));
	        		} catch (Exception e) {
					}
	        	}
	        	ret = line;
	        }

	        return ret;
	    }

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getData()
	 */
	public byte[] getData() {
	    return null;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getData(int, int)
	 */
	public byte[] getData(int start, int len) {
	    return null;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getField(net.sf.JRecord.Common.FieldDetail)
	 */
	public Object getField(IFieldDetail field) {

		if (field == null) return null;
	    return getFieldRaw(preferredLayout, field.getPos() - fieldStartingPos);
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getField(int, int)
	 */
	public Object getField(int recordIdx, int fieldIdx) {

		switch (fieldIdx) {
//		case Constants.FULL_LINE:	return getFullLine();
		case Constants.KEY_INDEX:	return null;
		}

        return getFieldRaw(recordIdx, fieldIdx);
    }

	protected Object getFieldRaw(int recordIdx, int fieldIdx) {

	    if (fields.size() > fieldIdx && fieldIdx >= 0) {
	    	//if (newRecord) System.out.println("Get (New) : " + fieldIdx + " " + fields.get(fieldIdx));
	        return fields.get(fieldIdx);
	    }
	    //if (newRecord) System.out.println("Get (New) : " + fieldIdx + " null");
	    return null;
	}

//	/**
//	 * @see net.sf.JRecord.Details.AbstractLine#getField(java.lang.String)
//	 */
//	public Object getField(String fieldName) {
//	    try {
//	    	return getField(preferredLayout,
//	    			layout.getRecord(preferredLayout).getFieldIndex(fieldName));
//	    } catch (Exception e) {
//			return null;
//		}
//	}


	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getFieldBytes(int, int)
	 */
	public byte[] getFieldBytes(int recordIdx, int fieldIdx) {
	    return null;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getFieldHex(int, int)
	 */
	public String getFieldHex(int recordIdx, int fieldIdx) {
	    return null;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getFieldText(int, int)
	 */
	public String getFieldText(int recordIdx, int fieldIdx) {
	    String s = "";
	    Object o;

	    if (fieldIdx < fields.size()
	    && (o = fields.get(fieldIdx)) != null) {
	        s = o.toString();
	    }
	    return s;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getFullLine()
	 */
	public String getFullLine() {
	    return "";
	}


	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getPreferredLayoutIdx()
	 */
	@Override
	public int getPreferredLayoutIdx() {
	    return preferredLayout;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#getPreferredLayoutIdx()
	 */
	@Override
	public int getPreferredLayoutIdxAlt() {
	    return preferredLayout;
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#replace(byte[], int, int)
	 */
	public void replace(byte[] rec, int start, int len) {
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setData(java.lang.String)
	 */
	public void setData(String newVal) {
	    // TODO Auto-generated method stub
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setData(byte[])
	 */
	@Override
	public void setData(byte[] newVal) {
		// TODO Auto-generated method stub
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setField(net.sf.JRecord.Common.FieldDetail, java.lang.Object)
	 */
	public void setField(IFieldDetail field, Object value) throws RecordException {
    	if (field == null && (value == null || "".equals(value.toString()))) return;
		setRawField(preferredLayout, field.getPos(), value);
	}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setField(int, int, java.lang.Object)
	 */
	public void setField(int recordIdx, int fieldIdx, Object val)
			throws RecordException {
				setRawField(recordIdx, fieldIdx, val);
			}

//	private int getFieldNumber(int recordIdx, int fieldIdx) {
//	   	int idx = fieldIdx;
//
//	    //   	System.out.print("getField " + recordIdx + " " + fieldIdx);
//	       	if (useField4Index && recordIdx < layout.getRecordCount()
//	       	&& fieldIdx < layout.getRecord(recordIdx).getFieldCount()
//	       	&& layout.getRecord(recordIdx).getField(fieldIdx).getPos() >= 0) {
//	       		idx = layout.getRecord(recordIdx).getField(fieldIdx).getPos();
//	       	}
//	       	return idx;
//	}

	public void setRawField(int recordIdx, int fieldIdx, Object val)
			throws RecordException {

        for (int i = fields.size(); i <= fieldIdx; i++) {
            fields.add(null);
        }

        if (val != null || fields.get(fieldIdx) != null) {
        	fields.set(fieldIdx, val);
        }
    }


	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setFieldHex(int, int, java.lang.String)
	 */
	public String setFieldHex(int recordIdx, int fieldIdx, String val)
			throws RecordException {
			    // TODO Auto-generated method stub
			    return ""; //super.setFieldHex(recordIdx, fieldIdx, val);
			}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setFieldText(int, int, java.lang.String)
	 */
	public void setFieldText(int recordIdx, int fieldIdx, String value)
			throws RecordException {
				setField(recordIdx, fieldIdx, value);
			}

	/**
	 * @see net.sf.JRecord.Details.AbstractLine#setWriteLayout(int)
	 */
	public void setWriteLayout(int pWriteLayout) {
		preferredLayout = pWriteLayout;
		fields.set(XmlConstants.NAME_INDEX, layout.getRecord(preferredLayout).getRecordName());
	}

	/**
	 * @param pLayout The layouts to set.
	 */
	public void setLayout(final AbstractLayoutDetails pLayout) {
	//		System.out.print("set layout >> " + fields.get(0)
	//				+ " " + layout.getRecord(preferredLayout).getRecordName()
	//				+ " " + preferredLayout);
			preferredLayout = pLayout.getRecordIndex(layout.getRecord(preferredLayout).getRecordName());
	//		System.out.println(" " + preferredLayout + " --> " + pLayout.getRecord(preferredLayout).getRecordName());
			this.layout = (Layout) pLayout;
		}




	/**
	 * Test if Tree rebuild is required
	 */
	public boolean isRebuildTreeRequired() {
		boolean ret = rebuildRequired;
		rebuildRequired = false;
		return ret;
	}

	/**
	 * @return the children
	 */
	public final AbstractTreeDetails<FieldDef, RecordDef, Layout, ArrayListLine<FieldDef, RecordDef, Layout>> getTreeDetails() {
		return children;
	}

	/* (non-Javadoc)
	 * @see net.sf.JRecord.Common.AbstractChildLines#isRebuildTreeRequired()
	 */
	@Override
	public boolean isError() {

		return false;
	}


	@SuppressWarnings("rawtypes")
	@Override
	public ArrayListLine getNewDataLine() {
		return (ArrayListLine) clone();
	}

	protected final AbstractRecordDetail.FieldDetails getFieldFromName(String fieldName) {
		AbstractRecordDetail.FieldDetails fldDef = null;
		if (preferredLayout >= 0) {
			fldDef = layout.getRecord(preferredLayout).getField(fieldName);
		}
		return fldDef;
	}

	@Override
	public boolean isDefined(int rec, int pos) {

		return fields != null && pos < fields.size() && fields.get(pos) != null;
	}
	
	
}