/*
 * Changes
 *
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Changed to store values in a ExternalField variable
 *     rather than local class variables
 */

package net.sf.RecordEditor.re.db.Record;

import net.sf.JRecord.External.ExternalField;
import net.sf.RecordEditor.utils.jdbc.AbsRecord;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select
 *              FieldPos as  Pos,
 *              FieldLength as Len,
 *              FieldName as Name,
 *              Description,
 *              FieldType as Type,
 *              DecimalPos as Decimal,
 *              Cell_Format cellFormat,
 *              Parameter parameter,
 *              DefaultValue as Default,
 *              CobolName,
 *              RECORD_STYLE,
 *              SubKey
 *       From Tbl_RF_RecordFields
 *       where RecordId = ?
 *       order by FieldPos, FieldLength Desc
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class RecordFieldsRec extends AbsRecord {

  protected int initSubKey ;


  private ExternalField value;

  /**
   * Create an blank field
   *
   */
  public RecordFieldsRec () {
      super();
      value = new ExternalField();
      setExternalValue(value);
      setKeys();
  }

  /**
   * Create a standard field
   * @param pPos
   * @param pLen
   * @param pName
   * @param pDescription
   * @param pType
   * @param pDecimal
   * @param pCellFormat
   * @param pParameter
   * @param pDefault
   * @param pCobolName
   * @param pSubKey
   */
  public RecordFieldsRec(
                    int pPos
                  , int pLen
                  , String pName
                  , String pDescription
                  , int pType
                  , int pDecimal
                  , int pCellFormat
                  , String pParameter
                  , String pDefault
                  , String pCobolName
                  , int pSubKey
                  ) {
      this(new ExternalField(pPos
              , pLen
              , pName
              , pDescription
              , pType
              , pDecimal
              , pCellFormat
              , pParameter
              , pDefault
              , pCobolName
              , pSubKey));
  }


  /**
   * create a DB field value from an external field
   * @param field field values
   */
  public RecordFieldsRec(final ExternalField field) {
      super(false);

      value = field;
      setExternalValue(value);
      setKeys();
  }

  /**
   *  This method copies the key fields to the Init* fields
   */
  public void setKeys() {

      initSubKey = value.getSubKey();
  }





  /**
 * @see net.sf.RecordEditor.utils.jdbc.AbsRecord#hasTheKeyChanged()
 */
@Override
public boolean hasTheKeyChanged() {
	return initSubKey != value.getSubKey();
}

/**
   *  This method returns clones the current record
   *
   *  @return a duplicate of the current record
   */
  public Object clone() {

      super.clone();

      RecordFieldsRec ret = new RecordFieldsRec(
                        value.fullClone()
                    );

      ret.setNew(true);
      ret.setUpdateStatus(UPDATED);

      return ret;
  }



  /**
   *  This method returns clones the current record
   */
  public int getFieldCount() {
      return 11;
  }




  /**
   *  This method returns a field (specified by field number)
   *
   *  @param fieldNum the field number (in the record)
   *  @return the request field
   */
  public Object getField(int fieldNum) {

      if (updateStatus == NULL_INT_VALUE) return "";

      switch (fieldNum) {
        case (0)  : return Integer.valueOf(value.getPos());
        case (1)  : return Integer.valueOf(value.getLen());
        case (2)  : return value.getName();
        case (3)  : return value.getDescription();
        case (4)  : return Integer.valueOf(value.getType());
        case (5)  : return Integer.valueOf(value.getDecimal());
        case (6)  : return Integer.valueOf(value.getCellFormat());
        case (7)  : return value.getParameter();
        case (8)  : return value.getDefault();
        case (9)  : return value.getCobolName();
        case (10) : return Integer.valueOf(value.getSubKey());
        default   : return "";
      }
  }


  /**
   *  This method sets a field (specified by field number) with a string value
   *
   *  @param fieldNum the field number (in the record)
   *  @param val the value to be assigned to the field
   */
  protected void setFieldWithString(int fieldNum, String val) {

      switch (fieldNum) {
        case (0) : value.setPos(cnvToInt(value.getPos(), val, "Position" ));
        break;
        case (1) : value.setLen(cnvToInt(value.getLen(), val, "Length" ));
        break;
        case (2) : value.setName(val);
        break;
        case (3) : value.setDescription(val);
        break;
        case (4) : value.setType(cnvToInt(value.getType(), val, "FieldType" ));
        break;
        case (5) : value.setDecimal(cnvToInt(value.getDecimal(), val, "DecimalPos" ));
        break;
        case (6) : value.setCellFormat(cnvToInt(value.getCellFormat(), val, "Cell_Format" ));
        break;
        case (7) : value.setParameter(val);
        break;
        case (8) : value.setDefault(val);
        break;
        case (9) : value.setCobolName(val);
        break;
        case (10) : value.setSubKey(cnvToInt(value.getSubKey(), val, "Field Id" ));
        break;
        default  : ;
      }
  }


  /**
   *  This method sets a field (specified by field number) with an object value
   *
   *  @param fieldNum the field number (in the record)
   *  @param val the value to be assigned to the field
   */
  protected void setFieldWithObject(int fieldNum, Object val) {

      switch (fieldNum) {
        case (0) : value.setPos(((Integer) val).intValue());
        break;
        case (1) : value.setLen(((Integer) val).intValue());
        break;
        case (4) : value.setType(((Integer) val).intValue());
        break;
        case (5) : value.setDecimal(((Integer) val).intValue());
        break;
        case (6) : value.setCellFormat(((Integer) val).intValue());
        break;
        case (10) : value.setSubKey(((Integer) val).intValue());
        break;
        default  : setFieldWithString(fieldNum, (String) val) ;
      }
  }


  /**
   * @return Returns the value.
   */
  public ExternalField getValue() {
      return value;
  }
}
