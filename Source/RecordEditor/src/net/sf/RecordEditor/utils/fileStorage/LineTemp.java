package net.sf.RecordEditor.utils.fileStorage;


import net.sf.JRecord.Common.IFieldDetail;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Common.RecordRunTimeException;
import net.sf.JRecord.Details.LayoutDetail;


public class LineTemp extends LineBase {



	public LineTemp(LayoutDetail group, FileChunkLine fileChunk, int line) {
		super(group, fileChunk, line);
	}

	@Override
	protected void clearData() {
		throw new RecordRunTimeException(CAN_NOT_UPDATE_TEMPORARY_LINE);
	}

	@Override
	public void setData(byte[] newVal) {
		throw new RecordRunTimeException(CAN_NOT_UPDATE_FIELD_IN_TEMPORARY_LINE);
	}

	@Override
	public void setField(IFieldDetail field, Object value)
			throws RecordException {
		throw new RecordException(CAN_NOT_UPDATE_FIELD_IN_TEMPORARY_LINE);
	}

	@Override
	public String setFieldHex(int recordIdx, int fieldIdx, String val)
			throws RecordException {
		throw new RecordException(CAN_NOT_UPDATE_FIELD_IN_TEMPORARY_LINE);
	}

	@Override
	public void setFieldText(int recordIdx, int fieldIdx, String value)
			throws RecordException {
		throw new RecordException(CAN_NOT_UPDATE_FIELD_IN_TEMPORARY_LINE);
	}



}
