package net.sf.RecordEditor.re.db.Table;

import net.sf.RecordEditor.utils.jdbc.AbsRecord;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select TblKey, Details
 *       From   Tbl_TI_IntTbls
 *       Where  TblId = ?
 *       Order By TblKey
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public final class TableRec extends AbsRecord {

  private int tblKey;
  protected int initTblKey ;
  private String details, foreignName = "";



  public TableRec () {
      super();

      tblKey = 0;
      details = "";

      setKeys();
  }

  public TableRec (
                    int pTblKey
                  , String pDetails
                  ) {
      super(false);

      tblKey = pTblKey;
      details = pDetails;
      foreignName = details;

      setKeys();
  }

//  public TableRec (
//          int pTblKey
//        , String pDetails
//        , String foreignNameStr
//        ) {
//	  super(false);
//
//	  tblKey = pTblKey;
//	  details = pDetails;
//	  foreignName = foreignNameStr;
//
//	  setKeys();
//  }

  /**
   *  This method copies the key fields to the Init* fields
   */
  public void setKeys() {

      initTblKey = tblKey;
  }




  /**
   * @see net.sf.RecordEditor.utils.jdbc.AbsRecord#hasTheKeyChanged()
   */
  @Override
  public boolean hasTheKeyChanged() {
	  return initTblKey != tblKey;
  }

/**
   *  This method returns clones the current record
   *
   *  @return a duplicate of the current record
   */
  public Object clone() {

      super.clone();

      TableRec ret = new TableRec(
                        tblKey
                      , details
                    );

      ret.setNew(true);
      ret.setUpdateStatus(UPDATED);

      return ret;
  }



  /**
   *  This method returns clones the current record
   */
  public int getFieldCount() {
      return 2;
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
        case (0) : return Integer.valueOf(tblKey);
        case (1) : return details;
        case (2) : return foreignName;
        default  : return "";
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
        case (0) : setTblKey(cnvToInt(tblKey, val, "TblKey" ));		break;
        case (1) : setDetails(val);									break;
        case (2) : foreignName = val;								break;
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
        case (0) : setTblKey(((Integer) val).intValue());
        break;
        default  : setFieldWithString(fieldNum, (String) val) ;
      }
  }

  /**
   *  This method gets the vaule of TblKey
   */
  public int getTblKey() {
      return tblKey;
  }

  /**
   *  This method sets the vaule of TblKey
   *
   * @param val value to be assigned to TblKey
   */
  public void setTblKey(int val) {

      if ((val != tblKey) || (updateStatus == NULL_INT_VALUE)) {
           tblKey = val;
           updateStatus = UPDATED;
      }
  }

  /**
   *  This method gets the vaule of Details
   */
  public String getDetails() {
      return details;
  }

  /**
   *  This method sets the vaule of Details
   *
   * @param val value to be assigned to Details
   */
  public void setDetails(String val) {

      if ((val == null || "".equals(val))
      && (details == null || "".equals(details))) {
          return;
      }

      if ((val == null) || (! val.equals(details)) || (updateStatus == NULL_INT_VALUE)) {
           details = val;
           updateStatus = UPDATED;
      }
  }

}
