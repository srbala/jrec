package net.sf.RecordEditor.utils.protoGen.cobolOpt;
// Generated by proto2javame, Thu Aug 22 17:40:27 EST 2013.

import java.io.IOException;
import java.io.InputStream;
import java.util.Vector;

import net.jarlehansen.protobuf.javame.AbstractOutputWriter;
import net.jarlehansen.protobuf.javame.ComputeSizeUtil;
import net.jarlehansen.protobuf.javame.UninitializedMessageException;
import net.jarlehansen.protobuf.javame.input.DelimitedInputStream;
import net.jarlehansen.protobuf.javame.input.DelimitedSizeUtil;
import net.jarlehansen.protobuf.javame.input.InputReader;
import net.jarlehansen.protobuf.javame.input.taghandler.DefaultUnknownTagHandlerImpl;
import net.jarlehansen.protobuf.javame.input.taghandler.UnknownTagHandler;
import net.jarlehansen.protobuf.javame.output.OutputWriter;

public final class CobolCopybookOption extends AbstractOutputWriter {
	private static UnknownTagHandler unknownTagHandler = DefaultUnknownTagHandlerImpl.newInstance();

	private final int cobolDialect;
	private static final int fieldNumberCobolDialect = 1;

	private final int fileStructure;
	private static final int fieldNumberFileStructure = 2;

	private final int splitOption;
	private static final int fieldNumberSplitOption = 3;

	private final String font;
	private static final int fieldNumberFont = 4;

	private final String copybookDir;
	private static final int fieldNumberCopybookDir = 5;

	private final String copybookName;
	private static final int fieldNumberCopybookName = 6;

	private final long copybookDateTime;
	private static final int fieldNumberCopybookDateTime = 7;

	private final java.util.Vector recordExpressions;
	private static final int fieldNumberRecordExpressions = 15;


	public static Builder newBuilder() {
		return new Builder();
	}

	private CobolCopybookOption(final Builder builder) {
		if (builder.hasCobolDialect && builder.hasFileStructure && builder.hasSplitOption && builder.hasFont && builder.hasCopybookDir && builder.hasCopybookName && builder.hasCopybookDateTime ) {
			this.cobolDialect = builder.cobolDialect;
			this.fileStructure = builder.fileStructure;
			this.splitOption = builder.splitOption;
			this.font = builder.font;
			this.copybookDir = builder.copybookDir;
			this.copybookName = builder.copybookName;
			this.copybookDateTime = builder.copybookDateTime;
			this.recordExpressions = builder.recordExpressions;
		} else {
			throw new UninitializedMessageException("Not all required fields were included (false = not included in message), " +
				" cobolDialect:" + builder.hasCobolDialect + " fileStructure:" + builder.hasFileStructure + " splitOption:" + builder.hasSplitOption + " font:" + builder.hasFont + " copybookDir:" + builder.hasCopybookDir + " copybookName:" + builder.hasCopybookName + " copybookDateTime:" + builder.hasCopybookDateTime + "");
		}
	}

	public static class Builder {
		private int cobolDialect;
		private boolean hasCobolDialect = false;

		private int fileStructure;
		private boolean hasFileStructure = false;

		private int splitOption;
		private boolean hasSplitOption = false;

		private String font;
		private boolean hasFont = false;

		private String copybookDir;
		private boolean hasCopybookDir = false;

		private String copybookName;
		private boolean hasCopybookName = false;

		private long copybookDateTime;
		private boolean hasCopybookDateTime = false;

		private java.util.Vector recordExpressions = new java.util.Vector();
		private boolean hasRecordExpressions = false;


		private Builder() {
		}

		public Builder setCobolDialect(final int cobolDialect) {
			this.cobolDialect = cobolDialect;
			this.hasCobolDialect = true;
			return this;
		}

		public Builder setFileStructure(final int fileStructure) {
			this.fileStructure = fileStructure;
			this.hasFileStructure = true;
			return this;
		}

		public Builder setSplitOption(final int splitOption) {
			this.splitOption = splitOption;
			this.hasSplitOption = true;
			return this;
		}

		public Builder setFont(final String font) {
			this.font = font;
			this.hasFont = true;
			return this;
		}

		public Builder setCopybookDir(final String copybookDir) {
			this.copybookDir = copybookDir;
			this.hasCopybookDir = true;
			return this;
		}

		public Builder setCopybookName(final String copybookName) {
			this.copybookName = copybookName;
			this.hasCopybookName = true;
			return this;
		}

		public Builder setCopybookDateTime(final long copybookDateTime) {
			this.copybookDateTime = copybookDateTime;
			this.hasCopybookDateTime = true;
			return this;
		}

		public Builder setRecordExpressions(final java.util.Vector recordExpressions) {
			if(!hasRecordExpressions) {
				hasRecordExpressions = true;
			}
			this.recordExpressions = recordExpressions;
			return this;
		}


		public Builder addElementRecordExpressions(final RecordCheck element) {
			if(!hasRecordExpressions) {
				hasRecordExpressions = true;
			}
			recordExpressions.addElement(element);
			return this;
		}

		public CobolCopybookOption build() {
			return new CobolCopybookOption(this);
		}
	}

	public int getCobolDialect() {
		return cobolDialect;
	}

	public int getFileStructure() {
		return fileStructure;
	}

	public int getSplitOption() {
		return splitOption;
	}

	public String getFont() {
		return font;
	}

	public String getCopybookDir() {
		return copybookDir;
	}

	public String getCopybookName() {
		return copybookName;
	}

	public long getCopybookDateTime() {
		return copybookDateTime;
	}

	public java.util.Vector getRecordExpressions() {
		return recordExpressions;
	}

	public String toString() {
		final String TAB = "   ";
		String retValue = "";
		retValue += this.getClass().getName() + "(";
		retValue += "cobolDialect = " + this.cobolDialect + TAB;
		retValue += "fileStructure = " + this.fileStructure + TAB;
		retValue += "splitOption = " + this.splitOption + TAB;
		retValue += "font = " + this.font + TAB;
		retValue += "copybookDir = " + this.copybookDir + TAB;
		retValue += "copybookName = " + this.copybookName + TAB;
		retValue += "copybookDateTime = " + this.copybookDateTime + TAB;
		retValue += "recordExpressions = " + this.recordExpressions + TAB;
		retValue += ")";

		return retValue;
	}

	// Override
	public int computeSize() {
		int totalSize = 0;
		totalSize += ComputeSizeUtil.computeIntSize(fieldNumberCobolDialect, cobolDialect);
		totalSize += ComputeSizeUtil.computeIntSize(fieldNumberFileStructure, fileStructure);
		totalSize += ComputeSizeUtil.computeIntSize(fieldNumberSplitOption, splitOption);
		totalSize += ComputeSizeUtil.computeStringSize(fieldNumberFont, font);
		totalSize += ComputeSizeUtil.computeStringSize(fieldNumberCopybookDir, copybookDir);
		totalSize += ComputeSizeUtil.computeStringSize(fieldNumberCopybookName, copybookName);
		totalSize += ComputeSizeUtil.computeLongSize(fieldNumberCopybookDateTime, copybookDateTime);
		totalSize += computeNestedMessageSize();

		return totalSize;
	}

	private int computeNestedMessageSize() {
		int messageSize = 0;
		messageSize += ComputeSizeUtil.computeListSize(fieldNumberRecordExpressions, net.jarlehansen.protobuf.javame.SupportedDataTypes.DATA_TYPE_CUSTOM, recordExpressions);

		return messageSize;
	}

	// Override
	public void writeFields(final OutputWriter writer) throws IOException {
		writer.writeInt(fieldNumberCobolDialect, cobolDialect);
		writer.writeInt(fieldNumberFileStructure, fileStructure);
		writer.writeInt(fieldNumberSplitOption, splitOption);
		writer.writeString(fieldNumberFont, font);
		writer.writeString(fieldNumberCopybookDir, copybookDir);
		writer.writeString(fieldNumberCopybookName, copybookName);
		writer.writeLong(fieldNumberCopybookDateTime, copybookDateTime);
		writer.writeList(fieldNumberRecordExpressions, net.jarlehansen.protobuf.javame.SupportedDataTypes.DATA_TYPE_CUSTOM, recordExpressions);
		writer.writeData();
	}

	static CobolCopybookOption parseFields(final InputReader reader) throws IOException {
		int nextFieldNumber = getNextFieldNumber(reader);
		final CobolCopybookOption.Builder builder = CobolCopybookOption.newBuilder();

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
			case fieldNumberCobolDialect:
				builder.setCobolDialect(reader.readInt(fieldNumber));
				break;
			case fieldNumberFileStructure:
				builder.setFileStructure(reader.readInt(fieldNumber));
				break;
			case fieldNumberSplitOption:
				builder.setSplitOption(reader.readInt(fieldNumber));
				break;
			case fieldNumberFont:
				builder.setFont(reader.readString(fieldNumber));
				break;
			case fieldNumberCopybookDir:
				builder.setCopybookDir(reader.readString(fieldNumber));
				break;
			case fieldNumberCopybookName:
				builder.setCopybookName(reader.readString(fieldNumber));
				break;
			case fieldNumberCopybookDateTime:
				builder.setCopybookDateTime(reader.readLong(fieldNumber));
				break;
			case fieldNumberRecordExpressions:
				Vector vcRecordExpressions = reader.readMessages(fieldNumberRecordExpressions);
				for(int i = 0 ; i < vcRecordExpressions.size(); i++) {
					byte[] eachBinData = (byte[]) vcRecordExpressions.elementAt(i);
					RecordCheck.Builder builderRecordExpressions = RecordCheck.newBuilder();
					InputReader innerInputReader = new InputReader(eachBinData, unknownTagHandler);
					boolean boolRecordExpressions = true;
					int nestedFieldRecordExpressions = -1;
					while(boolRecordExpressions) {
						nestedFieldRecordExpressions = getNextFieldNumber(innerInputReader);
						boolRecordExpressions = RecordCheck.populateBuilderWithField(innerInputReader, builderRecordExpressions, nestedFieldRecordExpressions);
					}
					eachBinData = null;
					innerInputReader = null;
					builder.addElementRecordExpressions(builderRecordExpressions.build());
				}
				break;
		default:
			fieldFound = false;
		}
		return fieldFound;
	}

	public static void setUnknownTagHandler(final UnknownTagHandler unknownTagHandler) {
		CobolCopybookOption.unknownTagHandler = unknownTagHandler;
	}

	public static CobolCopybookOption parseFrom(final byte[] data) throws IOException {
		return parseFields(new InputReader(data, unknownTagHandler));
	}

	public static CobolCopybookOption parseFrom(final InputStream inputStream) throws IOException {
		return parseFields(new InputReader(inputStream, unknownTagHandler));
	}

	public static CobolCopybookOption parseDelimitedFrom(final InputStream inputStream) throws IOException {
		final int limit = DelimitedSizeUtil.readDelimitedSize(inputStream);
		return parseFields(new InputReader(new DelimitedInputStream(inputStream, limit), unknownTagHandler));
	}
}