package net.sf.RecordEditor.utils;

import net.sf.JRecord.Common.IFieldDetail;
import net.sf.JRecord.detailsSelection.AbsGroup;
import net.sf.JRecord.detailsSelection.AndSelection;
import net.sf.JRecord.detailsSelection.FieldSelect;
import net.sf.JRecord.detailsSelection.FieldSelectX;
import net.sf.JRecord.detailsSelection.OrSelection;
import net.sf.JRecord.detailsSelection.RecordSel;
import net.sf.JRecord.detailsSelection.Streamline;
import net.sf.RecordEditor.utils.common.Common;

public abstract class BaseSelectionBuilder {

	private OrSelection orSel = new OrSelection();
	private AndSelection andSel = new AndSelection();
	private AbsGroup retGroup = andSel;
	protected final IFieldDetail[] fields;
	protected final IFieldDetail[][] recFields;
	private boolean first = true;

	protected BaseSelectionBuilder(IFieldDetail[] fields, IFieldDetail[][] recFields) {
		super();
        this.fields = fields;
        this.recFields = recFields;
	}

	protected void add(RecordSel fs, int booleanOp) {

	    int boolOp = booleanOp;
	    if (first) {
	        boolOp = Common.BOOLEAN_OPERATOR_AND;
	        first = false;
	    } else if (boolOp == Common.BOOLEAN_OPERATOR_OR) {
	        orSel.add(andSel);
	        andSel = new AndSelection();
	    }

	    andSel.add(fs);
	}

	public final RecordSel build() {
	    RecordSel ret= andSel;
	    if (orSel.getSize() > 0) {
	        orSel.add(andSel);
	        ret = orSel;
	        retGroup = orSel;
	    }
	    return Streamline.getInstance().streamLine(ret);
	}

	/**
	 * @return the retGroup
	 */
	public AbsGroup getGroup() {
	    return retGroup;
	}

	protected FieldSelect getFieldDef(IFieldDetail field, String operator, String fieldValue) {
	    return FieldSelectX.get(field.getName(), fieldValue, operator, field);
	}

	protected FieldSelect getFieldDef(String fieldName, String operator, String fieldValue) {
	    return FieldSelectX.get(fieldName, fieldValue, operator, getFieldDef(fieldName));
	}

	protected RecordSel getFieldDef(int recNo, IFieldDetail fd, String operator, int summaryOp, String fieldValue, boolean caseSensitive) {
			    return FieldSelectX.get(fd.getName(), fieldValue, operator, summaryOp, recNo, fd, caseSensitive);
	}

	private IFieldDetail getFieldDef(String fieldName) {
	    IFieldDetail fieldDef = null;
	    if (fields != null && fieldName != null) {
	        for (IFieldDetail f : fields) {
	            if (fieldName.equalsIgnoreCase(f.getName())) {
	                fieldDef = f;
	                break;
	            }
	        }
	    }
	    return fieldDef;
	}

}