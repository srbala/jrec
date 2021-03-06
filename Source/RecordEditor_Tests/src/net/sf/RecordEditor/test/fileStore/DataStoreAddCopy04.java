package net.sf.RecordEditor.test.fileStore;

import junit.framework.TestCase;

import net.sf.RecordEditor.utils.fileStorage.FileDetails;



public class DataStoreAddCopy04 extends TestCase {
	
	private TestDataStoreAddCopy.IDataStoreCreator charCreator     = new TestDataStoreAddCopy.DataStoreCreator2(FileDetails.VARIABLE_LENGTH, FileDetails.CHAR_LINE);
	private TestDataStoreAddCopy.IDataStoreCreator fixedCreator    = new TestDataStoreAddCopy.DataStoreCreator2(FileDetails.VARIABLE_LENGTH, FileDetails.FIXED_LENGTH);
	private TestDataStoreAddCopy.IDataStoreCreator variableCreator1 
		= new TestDataStoreAddCopy.DataStoreCreator2(FileDetails.VARIABLE_LENGTH, TestDataStoreAddCopy.LARGE_VB);
	private TestDataStoreAddCopy.IDataStoreCreator variableCreator2 
		= new TestDataStoreAddCopy.DataStoreCreator2(TestDataStoreAddCopy.LARGE_VB, FileDetails.VARIABLE_LENGTH);
	private TestDataStoreAddCopy.IDataStoreCreator standardCreator 
			= new TestDataStoreAddCopy.DataStoreCreator2(FileDetails.VARIABLE_LENGTH, TestDataStoreAddCopy.STANDARD_STORAGE);
	
	
	public TestDataStoreAddCopy tst = new TestDataStoreAddCopy();
	


	public void testChar1() {
		tst.doTst("Char 1 ~", false, charCreator);
	}

	
	public void testFixed1() {
		tst.doTst("Fixed 1 ~", false, fixedCreator);
	}
	
	public void testVariable1() {
		tst.doTst("Large VB 1 ~", false,  variableCreator1);
	}
	
	public void testStandard1() {
		tst.doTst("Standard 1 ~", false,  standardCreator);
	}

	public void testChar2() {
		tst.doTst("Char 2 ~", true, charCreator);
	}
	
	public void testFixed2() {
		tst.doTst("Fixed 2 ~", true, fixedCreator);

	}
	
	public void testVariable2() {
		tst.doTst("LargeVB 2 ~", true, variableCreator1);
	}
	

	public void testStandard2() {
		tst.doTst("Standard 2 ~", true,  standardCreator);
	}

	
	public void testVariable3() {
		tst.doTst("Large VB 3 ~", false,  variableCreator2);
	}
	
	public void testVariable4() {
		tst.doTst("Large VB 4 ~", true, variableCreator2);
	}
}
