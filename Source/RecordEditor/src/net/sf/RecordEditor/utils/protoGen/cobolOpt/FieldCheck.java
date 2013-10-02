package net.sf.RecordEditor.utils.protoGen.cobolOpt;
// Generated by proto2javame, Wed Aug 21 10:58:39 EST 2013.

import java.io.IOException;
import java.io.InputStream;
import net.jarlehansen.protobuf.javame.UninitializedMessageException;
import net.jarlehansen.protobuf.javame.input.InputReader;
import net.jarlehansen.protobuf.javame.input.DelimitedInputStream;
import net.jarlehansen.protobuf.javame.input.DelimitedSizeUtil;
import net.jarlehansen.protobuf.javame.ComputeSizeUtil;
import net.jarlehansen.protobuf.javame.output.OutputWriter;
import net.jarlehansen.protobuf.javame.AbstractOutputWriter;
import net.jarlehansen.protobuf.javame.input.taghandler.UnknownTagHandler;
import net.jarlehansen.protobuf.javame.input.taghandler.DefaultUnknownTagHandlerImpl;

public final class FieldCheck extends AbstractOutputWriter {
	private static UnknownTagHandler unknownTagHandler = DefaultUnknownTagHandlerImpl.newInstance();

	private final int booleanOperator;
	private static final int fieldNumberBooleanOperator = 1;

	private final String fieldName;
	private static final int fieldNumberFieldName = 2;

	private final int operator;
	private static final int fieldNumberOperator = 3;

	private final String value;
	private static final int fieldNumberValue = 4;


	public static Builder newBuilder() {
		return new Builder();
	}

	private FieldCheck(final Builder builder) {
		if (builder.hasBooleanOperator && builder.hasFieldName && builder.hasOperator && builder.hasValue ) {
			this.booleanOperator = builder.booleanOperator;
			this.fieldName = builder.fieldName;
			this.operator = builder.operator;
			this.value = builder.value;
		} else {
			throw new UninitializedMessageException("Not all required fields were included (false = not included in message), " +
				" booleanOperator:" + builder.hasBooleanOperator + " fieldName:" + builder.hasFieldName + " operator:" + builder.hasOperator + " value:" + builder.hasValue + "");
		}
	}

	public static class Builder {
		private int booleanOperator;
		private boolean hasBooleanOperator = false;

		private String fieldName;
		private boolean hasFieldName = false;

		private int operator;
		private boolean hasOperator = false;

		private String value;
		private boolean hasValue = false;


		private Builder() {
		}

		public Builder setBooleanOperator(final int booleanOperator) {
			this.booleanOperator = booleanOperator;
			this.hasBooleanOperator = true;
			return this;
		}

		public Builder setFieldName(final String fieldName) {
			this.fieldName = fieldName;
			this.hasFieldName = true;
			return this;
		}

		public Builder setOperator(final int operator) {
			this.operator = operator;
			this.hasOperator = true;
			return this;
		}

		public Builder setValue(final String value) {
			this.value = value;
			this.hasValue = true;
			return this;
		}

		public FieldCheck build() {
			return new FieldCheck(this);
		}
	}

	public int getBooleanOperator() {
		return booleanOperator;
	}

	public String getFieldName() {
		return fieldName;
	}

	public int getOperator() {
		return operator;
	}

	public String getValue() {
		return value;
	}

	public String toString() {
		final String TAB = "   ";
		String retValue = "";
		retValue += this.getClass().getName() + "(";
		retValue += "booleanOperator = " + this.booleanOperator + TAB;
		retValue += "fieldName = " + this.fieldName + TAB;
		retValue += "operator = " + this.operator + TAB;
		retValue += "value = " + this.value + TAB;
		retValue += ")";

		return retValue;
	}

	// Override
	public int computeSize() {
		int totalSize = 0;
		totalSize += ComputeSizeUtil.computeIntSize(fieldNumberBooleanOperator, booleanOperator);
		totalSize += ComputeSizeUtil.computeStringSize(fieldNumberFieldName, fieldName);
		totalSize += ComputeSizeUtil.computeIntSize(fieldNumberOperator, operator);
		totalSize += ComputeSizeUtil.computeStringSize(fieldNumberValue, value);
		totalSize += computeNestedMessageSize();

		return totalSize;
	}

	private int computeNestedMessageSize() {
		int messageSize = 0;

		return messageSize;
	}

	// Override
	public void writeFields(final OutputWriter writer) throws IOException {
		writer.writeInt(fieldNumberBooleanOperator, booleanOperator);
		writer.writeString(fieldNumberFieldName, fieldName);
		writer.writeInt(fieldNumberOperator, operator);
		writer.writeString(fieldNumberValue, value);
	}

	static FieldCheck parseFields(final InputReader reader) throws IOException {
		int nextFieldNumber = getNextFieldNumber(reader);
		final FieldCheck.Builder builder = FieldCheck.newBuilder();

		while (nextFieldNumber > 0) {
			if(!populateBuilderWithField(reader, builder, nextFieldNumber)) {
				reader.getPreviousTagDataTypeAndReadContent();
			}
			nextFieldNumber = getNextFieldNumber(reader);
		}

		return builder.build();
	}

	static int getNextFieldNumber(final InputReader reader) throws IOException {
		return reader.getNextFieldNumber();
	}

	static boolean populateBuilderWithField(final InputReader reader, final Builder builder, final int fieldNumber) throws IOException {
		boolean fieldFound = true;
		switch (fieldNumber) {
			case fieldNumberBooleanOperator:
				builder.setBooleanOperator(reader.readInt(fieldNumber));
				break;
			case fieldNumberFieldName:
				builder.setFieldName(reader.readString(fieldNumber));
				break;
			case fieldNumberOperator:
				builder.setOperator(reader.readInt(fieldNumber));
				break;
			case fieldNumberValue:
				builder.setValue(reader.readString(fieldNumber));
				break;
		default:
			fieldFound = false;
		}
		return fieldFound;
	}

	public static void setUnknownTagHandler(final UnknownTagHandler unknownTagHandler) {
		FieldCheck.unknownTagHandler = unknownTagHandler;
	}

	public static FieldCheck parseFrom(final byte[] data) throws IOException {
		return parseFields(new InputReader(data, unknownTagHandler));
	}

	public static FieldCheck parseFrom(final InputStream inputStream) throws IOException {
		return parseFields(new InputReader(inputStream, unknownTagHandler));
	}

	public static FieldCheck parseDelimitedFrom(final InputStream inputStream) throws IOException {
		final int limit = DelimitedSizeUtil.readDelimitedSize(inputStream);
		return parseFields(new InputReader(new DelimitedInputStream(inputStream, limit), unknownTagHandler));
	}
}