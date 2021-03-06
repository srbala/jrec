/*
 * Changes
 *
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Changes due to changes in the RecordRec,
 *     creation of JRecord etc
 */

package net.sf.RecordEditor.re.db.Record;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import net.sf.JRecord.External.ExternalRecord;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.jdbc.AbsDB;
import net.sf.RecordEditor.utils.lang.LangConversion;

/**
 * This class provides DB Access using
 *
 *   <pre>
 *       Select
 *              RecordId,
 *              RecordName,
 *              Description,
 *              RecordType,
 *              System,
 *              ListChar,
 *              CopyBook,
 *              Delimiter,
 *              Quote,
 *              PosRecInd,
 *              RecSepList,
 *              RecordSep,
 *              Canonical_Name,
 *              Record_Style recordStyle,
 *              File_Structure fileStructure
 *       From Tbl_R_Records
 *
 *   </pre>
 * it also provides Insert / Update / Delete routines (depending on the options selected)
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 */

public class RecordDB  extends AbsDB<RecordRec> {


  private static final String[] COLUMN_NAMES = {
                   "Record Id"
                 , LangConversion.convert(LangConversion.ST_COLUMN_HEADING, "Record Name")
                 , LangConversion.convert(LangConversion.ST_COLUMN_HEADING,"Description")
                 , "Record Type"
                 , "System"
                 , "ListChar"
                 , "Cobol Copybook"
                 , "Delimiter"
                 , "Quote"
                 , "PosRecInd"
                 , "Record Seperator"
                 , "RecordSep"
                 , "Canonical_Name"
                 , "Record_Style"
                 , "File_Structure"
  };


  private PreparedStatement getMaxKey = null;

  public RecordDB() {

      resetSearch();

      sSQL = " Select  RecordId, RecordName, Description, RecordType, System, ListChar, CopyBook, Delimiter, Quote, PosRecInd, RecSepList, RecordSep, Canonical_Name, Record_Style, File_Structure";
      sFrom = "  From Tbl_R_Records";
      sWhereSQL = " ";
      sOrderBy = " ";
      updateSQL = "Update Tbl_R_Records  "
                   +  " Set RecordId= ? "
                   +  "   , RecordName= ? "
                   +  "   , Description= ? "
                   +  "   , RecordType= ? "
                   +  "   , System= ? "
                   +  "   , ListChar= ? "
                   +  "   , CopyBook= ? "
                   +  "   , Delimiter= ? "
                   +  "   , Quote= ? "
                   +  "   , PosRecInd= ? "
                   +  "   , RecSepList= ? "
                   +  "   , RecordSep= ? "
                   +  "   , Canonical_Name= ? "
                   +  "   , Record_Style= ? "
                   +  "   , File_Structure= ? "
                   +  " Where RecordId= ? "
                        ;

      deleteSQL = "Delete From  Tbl_R_Records  "
                   +  " Where RecordId= ? "
                        ;

      insertSQL = "Insert Into  Tbl_R_Records  ("
                      + "    RecordId"
                      + "  , RecordName"
                      + "  , Description"
                      + "  , RecordType"
                      + "  , System"
                      + "  , ListChar"
                      + "  , CopyBook"
                      + "  , Delimiter"
                      + "  , Quote"
                      + "  , PosRecInd"
                      + "  , RecSepList"
                      + "  , RecordSep"
                      + "  , Canonical_Name"
                      + "  , Record_Style"
                      + "  , File_Structure"
                      + ") Values ("
                      +    "     ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?   , ?"
                      + ")";

      super.columnNames = RecordDB.COLUMN_NAMES;
  }



  /**
   *  This method returns the next record (AbsRecord) from the cursor
   */
  //public AbsRecord absFetch() {
  //    return fetch();
  //}


  /**
   *  This method returns the next record from the cursor
   */
  public RecordRec fetch() {
  RecordRec ret = null;

      try {
    	  if (rsCursor == null) {
    		  super.open();
    	  }
          if (rsCursor.next()) {
        	  byte[] b = {};
        	  try {
        		  b = rsCursor.getString(12).getBytes();
        	  } catch (Exception e) {
        		  try {
        			  b = rsCursor.getBytes(12);
        		  } catch (Exception ex) {
				}
        	  }
             ret = new RecordRec(
                        rsCursor.getInt(1)
                      , fix(rsCursor.getString(2))
                      , rsCursor.getString(3)
                      , rsCursor.getInt(4)
                      , rsCursor.getInt(5)
                      , fix(rsCursor.getString(6))
                      , fix(rsCursor.getString(7))
                      , fix(rsCursor.getString(8))
                      , fix(rsCursor.getString(9))
                      , rsCursor.getInt(10)
                      , fix(rsCursor.getString(11))
                      , b
                      , fix(rsCursor.getString(13))
                      , rsCursor.getInt(14)
                      , rsCursor.getInt(15)
                      , false
                   );
          }
          message = "";
      } catch (Exception ex) {
           setMessage(ex.getMessage(), ex);
      }

      if (ret == null) {
    	  super.freeConnection();
      }

      return ret;
  }


  /**
   *  Get the number of columns returned by the SQL
   */
  public int getColumnCount() {
      return 16;
  }




  /* (non-Javadoc)
 * @see net.sf.RecordEditor.utils.jdbc.AbsDB#delete(net.sf.RecordEditor.utils.jdbc.AbsRecord)
 */
@Override
	public void delete(RecordRec val) {
		String   uSql;
		String   sSql  =
				  " select rs2.RECORDID, rs2.child_key"
				+ "   from  TBL_RS2_SUBRECORDS rs1 inner join TBL_RS2_SUBRECORDS rs2"
				+ "     on  rs1.RECORDID = rs2.RECORDID"
				+ "    and  rs2.PARENT_RECORDID = rs1.CHILD_ID"
				+ "  where  rs1.CHILD_RECORD = " + val.getRecordId();
		String[] updSql  = {
//					  " Update  TBL_RS2_SUBRECORDS rs3 "
//			        + "    set PARENT_RECORDID = -1 "
//					+ "  where rs3.child_key in "
//					+ "    (select rs2.child_key from    TBL_RS2_SUBRECORDS rs1"
//					+ "                      inner join  TBL_RS2_SUBRECORDS rs2"
//					+ "                              on  rs1.RECORDID = rs2.RECORDID"
//					+ "                             and  rs2.PARENT_RECORDID = rs1.CHILD_ID"
//					+ "                           where  rs1.CHILD_RECORD = " + val.getRecordId()
//					+ "                             and  rs1.RECORDID = rs3.RECORDID"
//					+ "                             and  rs2.RECORDID = rs3.RECORDID)",
					  "Delete from  TBL_RS2_SUBRECORDS where CHILD_RECORD = " + val.getRecordId(),
					  "Delete from  TBL_RFS_FIELDSELECTION where RECORDID = " + val.getRecordId(),
					  "Delete from  TBL_RF1_RECORDFIELDS where RECORDID = " + val.getRecordId(),
					  "Delete from  TBL_RS2_SUBRECORDS where RECORDID = " + val.getRecordId(),
		};
		
		val.setKeys();

		try {
			ResultSet resultset = connect.getUpdateConnection().createStatement().executeQuery(sSql);
			while (resultset.next()) {
				uSql = " Update  TBL_RS2_SUBRECORDS rs3 "
				     + "    set PARENT_RECORDID = -1 "
					 + "  Where RecordId   = " + resultset.getString(1)
					 +    " and  child_key = " + resultset.getString(2);
				connect.getUpdateConnection().createStatement().execute(uSql);
			}
		} catch (Exception e) {
			Common.logMsgRaw(sSql, null);
			Common.logMsgRaw(UPDATE_FAILED + e.getClass().getName() + " " + e.getMessage(), e);
			e.printStackTrace();
		}

		for (String sql : updSql) {
			try {
				connect.getUpdateConnection().createStatement().execute(sql);
			} catch (Exception e) {
				Common.logMsgRaw(sql, null);
				Common.logMsgRaw(UPDATE_FAILED + e.getClass().getName() + " " + e.getMessage(), e);
				e.printStackTrace();
			}
		}

		super.delete(val);
	}



/**
   *  This method resets the search Arguments
   *
   */
  public void resetSearch() {

      super.resetSearch();
      sep = " Where ";
      sqlCursor = null;
  }


  /**
   *  This method sets a search argument for RecordName
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchRecordName(String operator, String val) {

      setSearchStrArg("RecordName", operator, val);

  }


  /**
   *  This method sets a search argument for RecordName
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchRecordId(String operator, int val) {

      setSearchArg("RecordId", operator, val);
  }

  /**
   *  This method sets a search argument for Description
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchDescription(String operator, String val) {

      setSearchStrArg("Description", operator, val);

  }



  /**
   *  This method sets a search argument for RecordType
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchRecordType(String operator, int val) {

      sWhere = sWhere + sep + "RecordType" + operator + val;
      sep = "   and ";

  }



  /**
   *  This method sets a search argument for System
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchSystem(String operator, int val) {

      sWhere = sWhere + sep + "System" + operator + val;
      sep = "   and ";

  }



  /**
   *  This method sets a search argument for ListChar
   *
   * @param operator operator to be used in the where clause
   * @param val value to be used in the search
   */
  public void setSearchListChar(String operator, String val) {

      setSearchStrArg("ListChar", operator, val);

  }




  /**
   *
   * @param statement statement that needs parameteres set
   * @param value Value to assign to the Statement parameters
   * @param idx parameter index
   *
   * @return updated index
   * @throws SQLException SQL error
   */
  @SuppressWarnings("deprecation")
protected int setSQLParams(PreparedStatement statement, RecordRec value, boolean insert, int idx)
                             throws SQLException {
      //RecordRec valueX = value;
      ExternalRecord val = value.getValue();

      statement.setInt(idx++, val.getRecordId());
      statement.setString(idx++, correctStr(val.getRecordName()));
      statement.setString(idx++, correctStr(val.getDescription()));
      statement.setInt(idx++, val.getRecordType());
      statement.setInt(idx++, val.getSystem());
      statement.setString(idx++, correctStr(val.getListChar()));
      statement.setString(idx++, correctStr(val.getCopyBook()));
      statement.setString(idx++, correctStr(val.getDelimiter()));
      statement.setString(idx++, correctStr(val.getQuote()));
      statement.setInt(idx++, val.getPosRecInd());
      statement.setString(idx++, correctStr(val.getRecSepList()));
      statement.setString(idx++, new String(correctBytes(val.getRecordSep())));
      statement.setString(idx++, correctStr(val.getFontName()));
      statement.setInt(idx++, val.getRecordStyle());
      statement.setInt(idx++, val.getFileStructure());


      return idx;
  }


  /**
   * Setup the where parameters
   *
   * @param statement SQL statement
   * @param value Value to assign to the Statement parameters
   * @param idx current index
   * @throws SQLException SQL error
   */
  protected void setWhere(PreparedStatement statement, RecordRec value, int idx)
                          throws SQLException {
      statement.setInt(idx, value.getInitRecordId());
  }

  /**
   * This method gets the next key
   */
  private int getNextKey() {
      final String sql = "Select max(RecordId) From  Tbl_R_Records "
                 ;
      int ret = 1;

      try {
          if (isPrepareNeeded(getMaxKey)) {
              getMaxKey = connect.getConnection().prepareStatement(sql);
          }

          ResultSet rsKey = getMaxKey.executeQuery();
          if (rsKey.next()) {
              ret = rsKey.getInt(1) + 1;
          }
          rsKey.close();
          message = "";
     } catch (Exception ex) {
          setMessage(sql, ex.getMessage(), ex);
     }

    return ret;
  }





  /**
   *  This method inserts one record
   *
   *  @param val value to be inserted
   */
  public void insert(RecordRec value) {
      //RecordRec val = (RecordRec) value;

	  //System.out.print("  Record DB 1");
      int i = 0;
      //System.out.print("  Record DB 2");
      boolean free = super.isSetDoFree(false);

      int key = getNextKey();

      //System.out.print("  Record DB 3");
      value.getValue().setRecordId(key++);
      //System.out.print("  Record DB 4");
      while ((i++ < 10) && (! tryToInsert(value))) {
          value.getValue().setRecordId(key++);
      }
      super.setDoFree(free);
  }




/**
 *   Close the prepared statments
 */
 public void fullClose() {

     super.fullClose();

     closeStatement(getMaxKey);

 }

 private String fix(String s) {
	 if (s == null) {
		 return null;
	 }
	 return s.trim();
 }
}
