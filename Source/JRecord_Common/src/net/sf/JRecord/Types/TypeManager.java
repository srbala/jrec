/*
 * @Author Bruce Martin
 * Created on 28/08/2005
 *
 * Purpose: Act as a repository for type definitions
 *
 * Modification log:
 * On 2006/06/28 by Jean-Francois Gagnon:
 *    - Adjusted the type manager so it can manage the
 *      Fujitsu Zoned Decimal as well as the Sign Separate Numeric
 *
 * # Version 0.60 Bruce Martin 2007/02/16
 *   - Starting to seperate the Record package out from the RecordEditor
 *     so that it can be used seperately. So classes have been moved
 *     to the record package (ie RecordException + new Constant interface
 *   - Added new Date and Checkbox types
 */
package net.sf.JRecord.Types;

import net.sf.JRecord.Common.RecordException;
//import net.sf.RecordEditor.record.format.CellFormat;

/**
 * This class stores / retrieves type definitions and format definitions
 * i.e. it is a repository for type and format definitions.
 *
 * <p>It also stores the system TypeManager
 * (retrieved via method <b>getSystemTypeManager</b>).
 *
 * @author Bruce Martin
 *
 * @version 0.55
 */
public class TypeManager {

    public static final int SYSTEM_ENTRIES = 120;

    public static final int INVALID_INDEX  = SYSTEM_ENTRIES - 1;


    private Type[] types;

    private Type charType    = new TypeChar(true);

    private int userSize;

    private static TypeManager systemTypeManager = null;


    /**
     * This class stores / retrieves types definitions
     */
    public TypeManager() {
        this(true, Type.DEFAULT_USER_RANGE_SIZE);
    }


    /**
     *  This class stores / retrieves types definitions
     *
     * @param addSystemTypes add the system types
     * @param numberOfUserTypes number of user types to be allowed
     */
    public TypeManager(final boolean addSystemTypes,
            		   final int numberOfUserTypes) {
        super();

        int i;

        userSize  = numberOfUserTypes;

        if (userSize < 0) {
            userSize = 0;
        }

        types = new Type[SYSTEM_ENTRIES + userSize];

        for (i = 0; i < types.length; i++) {
            types[i] = charType;
        }

        if (addSystemTypes) {
            types[Type.ftCharRightJust]			= new TypeChar(false);
            types[Type.ftCharNullPadded]		= new TypeCharPadded();
            types[Type.ftCharNullTerminated]	= new TypeCharNullTerminated();

            types[Type.ftNumLeftJustified]		= new TypeNum(Type.ftNumLeftJustified);
            types[Type.ftNumRightJustified]		= new TypeNum(Type.ftNumRightJustified);
            types[Type.ftNumZeroPadded]			= new TypeNum(Type.ftNumZeroPadded);
            types[Type.ftAssumedDecimal]		= new TypeNum(Type.ftAssumedDecimal);
            types[Type.ftSignSeparateLead]		= new TypeSignSeparate(Type.ftSignSeparateLead);
            types[Type.ftSignSeparateTrail]		= new TypeSignSeparate(Type.ftSignSeparateTrail);
            types[Type.ftZonedNumeric]			= new TypeZoned();
            types[Type.ftNumAnyDecimal]			= new TypeNumAnyDecimal(false);
            types[Type.ftPositiveNumAnyDecimal]	= new TypeNumAnyDecimal(true);

            types[Type.ftFloat]					= new TypeFloat();
            types[Type.ftDouble]				= new TypeFloat();

            types[Type.ftPackedDecimal]			= new TypePackedDecimal();
            types[Type.ftDecimal]				= new TypeDecimalHex(Type.ftDecimal);
            types[Type.ftHex] 					= new TypeDecimalHex(Type.ftHex);

            types[Type.ftPostiveBinaryInt]		= new TypeBinLittleEndian(true);
            types[Type.ftBinaryInt]				= new TypeBinLittleEndian(false);
            types[Type.ftBinaryBigEndian]		= new TypeBinBigEndian(false);
            types[Type.ftPositiveBinaryBigEndian] = new TypeBinBigEndian(true);
            
            types[Type.ftRmComp]				= new TypeRmComp();
            types[Type.ftRmCompPositive]		= new TypeRmCompPositive();

            types[Type.ftBit]					= new TypeBit();

            types[Type.ftFjZonedNumeric]		= new TypeFjZoned();
            
//            types[Type.ftCharRestOfFixedRecord] = new TypeCharRestOfFixedRecord();
            types[Type.ftCharRestOfRecord]		= new TypeCharRestOfRecord();

        }
    }


    /**
     * register a type & format
     *
     * @param typeId type identifier of the type being top
     * @param typeDef type being registered
     *
     * @throws RecordException any error that occurs
     */
    public void registerType(int typeId, Type typeDef)
    throws RecordException {
        int idx = getIndex(typeId);

        if (idx == INVALID_INDEX) {
            throw new RecordException("Invalid Index Supplied " + typeId
                    + " Should be between " + Type.USER_RANGE_START
                    + " and " + (Type.USER_RANGE_START + userSize));
        }

        types[idx] = typeDef;
    }



    /**
     * Get a type Definition
     *
     * @param typeId type id to get the type definition for
     *
     * @return Type definition
     */
    public Type getType(int typeId) {
        return types[getIndex(typeId)];
    }


    /**
     * Adjusts the index
     *
     * @param type type supplied user
     *
     * @return adjusted index
     */
    public final int getIndex(int type) {
        int idx = INVALID_INDEX;

        if (type >= 0 && type < SYSTEM_ENTRIES) {
            idx = type;
        } else if (type >= Type.USER_RANGE_START
               &&  type <  Type.USER_RANGE_START + userSize) {
            idx =  type -  Type.USER_RANGE_START + SYSTEM_ENTRIES;
        }

        return idx;
    }
    
    /**
     * convert index back to type
     * @param index array index;
     * @return type number
     */
    public final int getTypeId(int index) {
    	int type = index;
    	if (index >= SYSTEM_ENTRIES) {
    		type = index - SYSTEM_ENTRIES + Type.USER_RANGE_START;
    	}
    	return type;
    }


    /**
     * Get the standard TypeManager
     * @return TypeManager
     */
    public static TypeManager getInstance() {
    	
	    if (systemTypeManager == null) {
	        systemTypeManager = new TypeManager();
	    }
		return systemTypeManager;
    }

    /**
     * Get the standard system Type Manager
     *
     * @return standard system Type Manager
     */
	public static TypeManager getSystemTypeManager() {
		return getInstance();
	}


	/**
	 * Set the standard system Type Manager
	 *
	 * @param pSystemTypeManager new type manager to use
	 */
	public static void setSystemTypeManager(TypeManager pSystemTypeManager) {
		TypeManager.systemTypeManager = pSystemTypeManager;
	}


    public final int getNumberOfTypes() {
        return types.length;
    }


	/**
	 * @return the userSize
	 */
	public final int getUserSize() {
		return userSize;
	}
}