package net.sf.RecordEditor.re.db.Table;

import java.sql.PreparedStatement;
import java.sql.SQLException;

import net.sf.RecordEditor.utils.jdbc.AbsDB;
import net.sf.RecordEditor.utils.jdbc.AbsRecord;
import net.sf.RecordEditor.utils.lang.LangConversion;



/**
 * This class provides DB Access using
 *
 *   <pre>
 *       Select TBlId,
 *              TblName,
 *              TblDescription as Description
 *       From   Tbl_T_Table
 *
 *   </pre>
 * it also provides Insert / Update / Delete routines (depending on the options selected)
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 */

public final class TableListDB  extends AbsDB<TableListRec> {


  private static final String[] COLUMN_NAMES = LangConversion.convertColHeading(
			"DB-TableList Columns",
			new String[] {
                   "Table Id"
                 , "Table Name"
                 , "Description"
  });



  public TableListDB() {

      resetSearch();

      sSQL = " Select  TBlId, TblName, TblDescription";
      sFrom = "  From   Tbl_T_Table";
      sWhereSQL = " ";
      sOrderBy = " ";
      updateSQL = "Update Tbl_T_Table  "
                   +  " Set TBlId= ? "
                   +  "   , TblName= ? "
                   +  "   , TblDescription= ? "
                   +  " Where TBlId= ? "
                        ;


      super.columnNames = TableListDB.COLUMN_NAMES;
  }



  /**
   *  This method returns the next record (AbsRecord) from the cursor
   */
  public AbsRecord absFetch() {
      return fetch();
  }


  /**
   *  This method returns the next record from the cursor
   */
  public TableListRec fetch() {
  TableListRec ret = null;

      try {
          if (rsCursor.next()) {
             ret = new TableListRec(
                        rsCursor.getInt(1)
                      , rsCursor.getString(2)
                      , rsCursor.getString(3)
                   );
          }
          message = "";
      } catch (Exception ex) {
           setMessage(ex.getMessage(), ex);
      }

      return ret;
  }


  /**
   *  Get the number of columns returned by the SQL
   */
  public int getColumnCount() {
      return 3;
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
  protected int setSQLParams(PreparedStatement statement, TableListRec value, boolean insert, int idx)
                             throws SQLException {

      statement.setInt(idx++, value.getTBlId());
      statement.setString(idx++, correctStr(value.getTblName()));
      statement.setString(idx++, correctStr(value.getDescription()));


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
  protected void setWhere(PreparedStatement statement, TableListRec value, int idx)
                          throws SQLException {

      statement.setInt(idx++, value.initTBlId);
  }

}
