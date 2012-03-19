package net.sf.RecordEditor.re.db.Combo;

import net.sf.RecordEditor.utils.jdbc.AbsRecord;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select Combo_Code, Combo_Value
 *       From   Tbl_CI_ComboItems
 *       Where  Combo_Id = ?
 *       Order By Combo_Code
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class ComboValuesRec extends AbsRecord {

  private String Combo_Code;
  protected String initCombo_Code ;
  private String Combo_Value;



  public ComboValuesRec () {
      super();

      Combo_Code = "";
      Combo_Value = "";

      setKeys();
  }

  public ComboValuesRec (
                    String pCombo_Code
                  , String pCombo_Value
                  ) {
      super(false);

      Combo_Code = pCombo_Code;
      Combo_Value = pCombo_Value;

      setKeys();
  }


  /**
   *  This method copies the key fields to the Init* fields
   */
  public void setKeys() {

      initCombo_Code = Combo_Code;
  }
  
  
  /**
   * @see net.sf.RecordEditor.utils.jdbc.AbsRecord#hasTheKeyChanged()
   */
  @Override
  public boolean hasTheKeyChanged() {
	  return initCombo_Code == null || !  initCombo_Code.equals(Combo_Code);
  }


/**
   *  This method returns clones the current record
   *
   *  @return a duplicate of the current record
   */
  public Object clone() {

      super.clone();

      ComboValuesRec ret = new ComboValuesRec(
                        Combo_Code
                      , Combo_Value
                    );

      ret.setNew(true);

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
        case (0) : return Combo_Code;
        case (1) : return Combo_Value;
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
        case (0) : setCombo_Code(val);
        break;
        case (1) : setCombo_Value(val);
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
        default  : setFieldWithString(fieldNum, (String) val) ;
      }
  }

  /**
   *  This method gets the vaule of Combo_Code
   */
  public String getCombo_Code() {
      return Combo_Code;
  }

  /**
   *  This method sets the vaule of Combo_Code
   *
   * @param val value to be assigned to Combo_Code
   */
  public void setCombo_Code(String val) {

      if ((val == null || "".equals(val))
      && (Combo_Code == null || "".equals(Combo_Code))) {
          return;
      }

      if ((val == null) || (! val.equals(Combo_Code)) || (updateStatus == NULL_INT_VALUE)) {
           Combo_Code = val;
           updateStatus = UPDATED;
      }
  }

  /**
   *  This method gets the vaule of Combo_Value
   */
  public String getCombo_Value() {
      return Combo_Value;
  }

  /**
   *  This method sets the vaule of Combo_Value
   *
   * @param val value to be assigned to Combo_Value
   */
  public void setCombo_Value(String val) {

      if ((val == null || "".equals(val))
      && (Combo_Value == null || "".equals(Combo_Value))) {
          return;
      }

      if ((val == null) || (! val.equals(Combo_Value)) || (updateStatus == NULL_INT_VALUE)) {
           Combo_Value = val;
           updateStatus = UPDATED;
      }
  }

}