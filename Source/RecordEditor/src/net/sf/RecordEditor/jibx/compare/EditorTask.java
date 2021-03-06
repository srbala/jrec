package net.sf.RecordEditor.jibx.compare;


public class EditorTask  {


	public static final String TASK_FILTER      = "Filter";
	public static final String TASK_SORT_TREE   = "SortTree";
	public static final String TASK_FIELD_TREE  = "FieldTree";
	public static final String TASK_SORT        = "Sort";
	public static final String TASK_RECORD_TREE = "RecordTree";
	public static final String TASK_VISIBLE_FIELDS = "VisibleFields";
	public static final String TASK_FIELD_SEQUENCE = "FieldSequence";

	public String type;
	public String layoutName="";
	public Layout filter = null;
	public SortTree sortTree = null;
	public RecordTree recordTree;
	public FieldSequence fieldSequence = null;


	public EditorTask setFilter(Layout filterDetails) {
		type = TASK_FILTER;

		filter = filterDetails;
		layoutName = filterDetails.name;

		return this;
	}


	public EditorTask setSortTree(String id, String recordLayoutName, SortTree sortDetails) {
		type = id;

		layoutName = recordLayoutName;
		sortTree = sortDetails;

		return this;
	}

	/**
	 * set Record Tree
	 * @param recordDetails record Tree
	 * @return this
	 */
	public EditorTask setRecordTree(String recordLayoutName, RecordTree recordDetails) {
		type = TASK_RECORD_TREE;

		layoutName = recordLayoutName;
		recordTree = recordDetails;

		return this;
	}


}
