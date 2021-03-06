/**
 *
 */
/*  -------------------------------------------------------------------------
 *
 *            Sub-Project: RecordEditor's version of JRecord 
 *    
 *    Sub-Project purpose: Low-level IO and record translation  
 *                        code + Cobol Copybook Translation
 *    
 *                 Author: Bruce Martin
 *    
 *                License: GPL 2.1 or later
 *                
 *    Copyright (c) 2016, Bruce Martin, All Rights Reserved.
 *   
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU General Public License
 *    as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *   
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 * ------------------------------------------------------------------------ */
      
package net.sf.JRecord.Details;

/**
 * Basic attribute class
 *
 * @author Bruce Martin
 *
 */
public class Attribute implements IAttribute {

	public static final Attribute FILE_STRUCTURE = new Attribute(TYPE_INT);
	private static int count;

	public final int id = count++;
	private final int type;



	public Attribute(int type) {
		super();
		this.type = type;
	}



	/* (non-Javadoc)
	 * @see net.sf.JRecord.Details.IAttribute#isStoredInMap()
	 */
	@Override
	public int getType() {
		return type;
	}

}
