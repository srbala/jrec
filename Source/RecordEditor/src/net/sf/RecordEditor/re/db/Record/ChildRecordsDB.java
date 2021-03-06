package net.sf.RecordEditor.re.db.Record;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import net.sf.JRecord.Log.AbsSSLogger;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.jdbc.AbsDB;
import net.sf.RecordEditor.utils.lang.LangConversion;



/**
 * This class provides DB Access using
 *
 *   <pre>
 *       Select
 *              Child_Record,
 *              Field_Start as Start,
 *              Field,
 *              Field_Value
 *       from Tbl_RS2_SubRecords
 *       where RecordId = ?
 *
 *   </pre>
 * it also provides Insert / Update / Delete routines (depending on the options selected)
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 */

public class ChildRecordsDB  extends AbsDB<ChildRecordsRec> {

	public static final String DB_NAME = "Tbl_RS2_SubRecords";
	private static final String[] COLUMN_NAMES = LangConversion.convertColHeading(
			"DB-ChildRecords columns",
			new String[] {
		"Child Record"
		, "Child Name"
		, "Field"
		, "Field Value"
		, "Tree Parent"
	});

	private static final String selectParentSql
			= "Select RecordId from " + DB_NAME 
			+ " where Child_Record=";
			
	private PreparedStatement delAllChildRecords = null;

	private int paramRecordId;

	public ChildRecordsDB() {

		resetSearch();

		sSQL = " Select  Child_Record, Field_Start, Field_Name, Field_Value, PARENT_RECORDID, "
			 +          "Child_Key, Operator_Sequence , default_Record, Child_Name , Child_Id ";
		sFrom = "  from " + DB_NAME;
		sWhereSQL = "  where RecordId = ?";
		sOrderBy = " Order by Child_Key";
		updateSQL = "Update " + DB_NAME
				+  " Set Child_Key= ? "
				+  "   , Child_Record= ? "
				+  "   , Field_Start= ? "
				+  "   , Field_Name= ? "
				+  "   , Field_Value= ? "
				+  "   , PARENT_RECORDID = ?"
				+  "   , Operator_Sequence = ?"
				+  "   , Default_Record = ?"
				+  "   , Child_Name = ?"
                + "    , Child_Id = ? "
				+  " Where RecordId= ? "
				+  "   and Child_Key= ? "
				;

		deleteSQL = "Delete From  " + DB_NAME
				+  " Where RecordId= ? "
				+  "   and Child_Key= ? "
				;

		insertSQL = "Insert Into  " + DB_NAME + "  ("
				+ "    Child_Key"
				+ "  , Child_Record"
				+ "  , Field_Start"
				+ "  , Field_Name"
				+ "  , Field_Value"
				+ "  , PARENT_RECORDID"
				+ "  , Operator_Sequence"
				+ "  , default_Record "
				+ "  , Child_Name"
                + "  , Child_Id"
				+ "  , RecordId"

                      + ") Values ("
                      +    "     ?   , ?   , ?   , ?   , ?, ?   , ?, ?, ?, ?, ?"
                      + ")";

		super.columnNames = ChildRecordsDB.COLUMN_NAMES;
	}


	/**
	 * sets up the DB parameters
	 *
	 * @param recordId
	 *
	 */
	public void setParams( int recordId) {

		paramRecordId = recordId;
	}

	public int getRecordId() {

		return paramRecordId;
	}

	/**
	 *  This method opens a SQL query
	 */
	public void open() {

		prepareCursor();

		try {
			sqlCursor.setInt(1, paramRecordId);

			setStringArgs(1);


			rsCursor  = sqlCursor.executeQuery();
			message = "";
		} catch (Exception ex) {
			setMessage(ex.getMessage(), ex);
		}
	}


	//  /**
	//   *  This method returns the next record (AbsRecord) from the cursor
	//   */
	//  public AbsRecord absFetch() {
	//      return fetch();
	//  }


	/**
	 *  This method returns the next record from the cursor
	 */
	public ChildRecordsRec fetch() {
		ChildRecordsRec ret = null;

		try {
			if (rsCursor.next()) {
				ret = new ChildRecordsRec(
						  rsCursor.getInt(1)
						, rsCursor.getInt(2)
						, rsCursor.getString(3)
						, rsCursor.getString(4)
						, rsCursor.getInt(5)
						, rsCursor.getInt(6)
						, rsCursor.getInt(7)
						, "Y".equalsIgnoreCase(rsCursor.getString(8))
						, rsCursor.getString(9)
						, rsCursor.getInt(10)
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
		return 5;
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
	protected int setSQLParams(PreparedStatement statement, ChildRecordsRec value, boolean insert, int idx)
			throws SQLException {
		ChildRecordsRec val = value;
		int childId = value.getChildId();
		String defaultRec = "N";

		if (value.isDefaultRecord()) {
			 defaultRec = "Y";
		}

		if (childId < 0) {
			final String sql = "Select max(Child_Id) From  Tbl_RS2_SubRecords "
					+  " Where RecordId= ? "
					;
			childId = getNextIntSubKey(sql, paramRecordId);
		}

		statement.setInt(idx++, val.getChildKey());
		statement.setInt(idx++, val.getChildRecordId());
		statement.setInt(idx++, val.getStart());
		statement.setString(idx++, correctStr(val.getField()));
		statement.setString(idx++, correctStr(val.getFieldValue()));
		statement.setInt(idx++, val.getParentRecord());
		statement.setInt(idx++, val.getOperatorSequence());
		statement.setString(idx++, defaultRec);
		statement.setString(idx++, val.getChildName());
		statement.setInt(idx++, childId);


		if (insert) {
			statement.setInt(idx++, paramRecordId);
		}

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
	protected void setWhere(PreparedStatement statement, ChildRecordsRec value, int idx)
			throws SQLException {
		//ChildRecordsRec val =  value;

		statement.setInt(idx++, paramRecordId);
		statement.setInt(idx++, value.initChildKey);
	}


	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.jdbc.AbsDB#delete(net.sf.RecordEditor.utils.jdbc.AbsRecord)
	 */
	@Override
	public void delete(ChildRecordsRec val) {

		String updSql  =
				  "Delete from  TBL_RFS_FIELDSELECTION "
				 + "where RECORDID = "  + paramRecordId
				 + "  and Child_Key = " + val.getChildKey();


		try {
			connect.getUpdateConnection().createStatement().execute(updSql);
		} catch (Exception e) {
			Common.logMsg(updSql, null);
			Common.logMsg(AbsSSLogger.ERROR, "Update Failed:", e.getClass().getName() + " " + e.getMessage(), e);
			e.printStackTrace();
		}


		super.delete(val);
	}


	/**
	 *  This method deletes all records matching the parameters
	 */
	public void deleteAll() {

		try {	
			open();
	    	boolean doDelete = fetch() != null;
	    	close();
	    	
	    	if (doDelete) {
				if (isPrepareNeeded(delAllChildRecords)) {
					delAllChildRecords = connect.getUpdateConnection().prepareStatement(
							"Delete From  " + DB_NAME
							+  " Where RecordId= ? "
							);
				}
	
				delAllChildRecords.setInt(1, paramRecordId);
	
				delAllChildRecords.executeUpdate();
				message = "";
	    	}
		} catch (Exception ex) {
			setMessage(ex.getMessage(), ex);
		} finally {
			freeConnection();
		}
	}




	/* (non-Javadoc)
	 * @see net.sf.RecordEditor.utils.jdbc.AbsDB#insert(net.sf.RecordEditor.utils.jdbc.AbsRecord)
	 */
	@Override
	public void insert(ChildRecordsRec value) {
		int i = 0;
		boolean free = super.isSetDoFree(false);

		int key = getNextKey();

		value.setChildKey(key++);
		while ((i++ < 10) && (! tryToInsert(value))) {
			value.setChildKey(key++);
		}

		super.setDoFree(free);
	}


	/**
	 * This method gets the next key
	 */
	private int getNextKey() {
		final String sql = "Select max(Child_Key) From  Tbl_RS2_SubRecords "
				+  " Where RecordId= ? "
				;
		return getNextIntSubKey(sql, paramRecordId);
	}


	/**
	 *   Close the prepared statments
	 */
	public void fullClose() {

		super.fullClose();

		closeStatement(delAllChildRecords);

	}

	
	public List<Integer> getRecordsThatUse(int childRecordId) {
		String selectSql  = selectParentSql + childRecordId;
		ArrayList<Integer> ret = new ArrayList<Integer>();
		PreparedStatement cursor = null;
		ResultSet rs = null;

		try {
			cursor = connect.getConnection().prepareStatement(selectSql);
			rs = cursor.executeQuery();
			while (rs.next()) {
				ret.add(rs.getInt(1));
			}
		} catch (Exception e) {
			Common.logMsg(selectSql, null);
			Common.logMsg(AbsSSLogger.ERROR, "Read Failed:", e.getClass().getName() + " " + e.getMessage(), e);
			e.printStackTrace();
		} finally {
			if (cursor != null) {
				try {
					if (rs != null) {
						rs.close();
					}
					cursor.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}

		return ret;
	}
}
