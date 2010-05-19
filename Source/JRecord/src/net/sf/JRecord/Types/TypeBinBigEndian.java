/*
 * @Author Bruce Martin
 * Created on 6/09/2005
 *
 * Purpose: Type for Binary Integer - Big Endian (high to low format)
 *
 * Changes
 * # Version 0.56 Bruce Martin 2007/01/16
 *   - use isPostive method (instead of positive variable)
 *
 * # Version 0.60 Bruce Martin 2007/02/16
 *   - Starting to seperate the Record package out from the RecordEditor
 *     so that it can be used seperately. So classes have been moved
 *     to the record package (ie RecordException + new Constant interface)
 */
package net.sf.JRecord.Types;

import net.sf.JRecord.Common.Conversion;
import net.sf.JRecord.Common.FieldDetail;
import net.sf.JRecord.Common.RecordException;

/**
 * Type for Binary Integers - Big Endian (high to low format)
 *
 * @author Bruce Martin
 *
 * @version 0.55
 */
public class TypeBinBigEndian extends TypeNum {

    /**
     * Type for Binary Integers - Big Endian (high to low format)
     * <p>This class is the interface between the raw data in the file
     * and what is to be displayed on the screen for Big-Endian
     * binary integers.
     *
     * @param isPostive wether it is a positive integer
     */
    public TypeBinBigEndian(final boolean isPostive) {
        super(false, true, true, isPostive, true);
    }


    /**
     * @see net.sf.JRecord.Types.Type#getField(byte[], int, net.sf.JRecord.Common.FieldDetail)
     */
    public Object getField(byte[] record,
            			   final int position,
            			   final FieldDetail field) {
	    int pos = position - 1;
	    int min = java.lang.Math.min(field.getEnd(), record.length);

        String s;
        if (isPositive()) {
        	s = Conversion.getPositiveBigInt(record, pos, min - pos).toString();
        } else {
        	s = Conversion.getBigInt(record, pos, min - pos).toString();
        }

        s = addDecimalPoint(s, field.getDecimal());

        return s;
    }


    /**
     * @see net.sf.JRecord.Types.Type#setField(byte[], int, net.sf.JRecord.Common.FieldDetail, java.lang.Object)
     */
    public byte[] setField(byte[] record,
            			 final int position,
            			 final FieldDetail field, Object value)
            throws RecordException {

		int pos = position - 1;
		int len = field.getLen();
        String val = value.toString();

        formatValueForRecord(field, val);

        Conversion.setLong(record, pos, len,
                		   getBigDecimal(field, val).longValue(), isPositive());
        return record;
    }
}
