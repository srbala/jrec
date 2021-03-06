/*
 * Generated by XmplLineBuilder from Velocity template LineProcess.vm
 *
 */
package net.sf.RecordEditor.examples.genCode;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.zip.GZIPInputStream;

import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.IO.AbstractLineReader;
import net.sf.JRecord.IO.StandardLineReader;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.RecordEditor.utils.CopyBookDbReader;

/**
 * Generated by XmplLineBuilder from Velocity template LineProcess.vm
 *
 */
public class AmsReceiptProcess  {

    private int lineNumber;

    /**
     * process an input file
     *
     * @param fileName filename to process
     *
     * @throws IOException any IO error that occurs
     */
    public void process(String fileName)  throws IOException, RecordException {
        process(fileName, getGroup());
    }


    /**
     * process an input file
     *
     * @param fileName filename to process
     * @param group record layout
     *
     * @throws IOException any IO error that occurs
     */
    public void process(String fileName, LayoutDetail group)  
    throws IOException, RecordException {
        if (fileName.endsWith(".gz")) {
            FileInputStream rf = new FileInputStream(fileName);

            process(new GZIPInputStream(rf), group);

            rf.close();
        } else {
            process(new FileInputStream(fileName), group);
        }
    }

    /**
     * process an input stream
     *
     * @param file input stream process
     *
     * @throws IOException any IO error that occurs
     */
    public void process(InputStream file) throws IOException, RecordException {
        process(file, getGroup());
    }


    /**
     * get Record Layout
     *
     * @return Record Layout
     */
    private LayoutDetail getGroup() {
        return new CopyBookDbReader().getLayout("ams Receipt");
    }


    /**
     * process an input stream
     *
     * @param file input stream process
     * @param group record layout
     *
     * @throws IOException any IO error that occurs
     */
    public void process(InputStream file, LayoutDetail group) throws IOException, RecordException {
        int        preferedLayout;
        int         fileStructure = group.getFileStructure();
        LineIOProvider ioProvider = new LineIOProvider(new AmsReceiptProvider());
        AbstractLineReader      reader = ioProvider.getLineReader(fileStructure);
        AmsReceipt           line;

        lineNumber = 0;
        reader.open(file, group);
        fileOpen();

        while ((line = (AmsReceipt) reader.read()) != null) {
            preferedLayout = line.getPreferredLayoutIdx();
            lineNumber += 1;

            if (preferedLayout == AmsReceipt.getAmsReceiptFhHeaderIndex()) {
                processAmsReceiptFhHeader(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptRhReceiptHeaderIndex()) {
                processAmsReceiptRhReceiptHeader(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptRdReciptProductIndex()) {
                processAmsReceiptRdReciptProduct(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptRsReciptStoreIndex()) {
                processAmsReceiptRsReciptStore(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptAsIndex()) {
                processAmsReceiptAs(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptSoIndex()) {
                processAmsReceiptSo(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptScIndex()) {
                processAmsReceiptSc(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptApIndex()) {
                processAmsReceiptAp(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptArIndex()) {
                processAmsReceiptAr(line);
            } else if (preferedLayout == AmsReceipt.getAmsReceiptFtFileTrailerIndex()) {
                processAmsReceiptFtFileTrailer(line);
            } else {
                unkownRecord(line);
            }
        }

        fileClosed();
        reader.close();
    }


    /**
     * Called after file is opened
     */
    public void fileOpen() { }


    /**
     * Called after file is opened
     */
    public void fileClosed() { }


    /**
     * Called after file is opened
     *
     * @param line Line to be processed
     */
    public void unkownRecord(AmsReceipt line) { }



    /**
     * process "ams Receipt FH Header"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptFhHeader(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt RH Receipt Header"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptRhReceiptHeader(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt RD Recipt Product"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptRdReciptProduct(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt RS Recipt Store"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptRsReciptStore(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt AS"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptAs(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt SO"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptSo(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt SC"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptSc(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt AP"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptAp(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt AR"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptAr(AmsReceipt line)
    throws IOException { }


    /**
     * process "ams Receipt FT File Trailer"
     * $rec.Details.Description
     *
     * @param line Line to be processed
     *
     * @throws IOException any IO error that occurs
     */
    public void processAmsReceiptFtFileTrailer(AmsReceipt line)
    throws IOException { }


    /**
     * @return Returns the lineNumber.
     */
    public int getLineNumber() {
        return lineNumber;
    }
}
