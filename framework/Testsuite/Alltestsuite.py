import  unittest
from Package1.Tc_Logintest import Logintest
from Package1.Tc_Signuptest import Signuptest

from Package2.TC_Paymenttest import PymentTesting
from  Package2.TC_paymentReturnTest import Test
#loading testcases
tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(Signuptest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PymentTesting)
tc4=unittest.TestLoader().loadTestsFromTestCase(Test)
tc5=unittest.TestLoader().loadTestsFromTestCase(Test)
#Creating Test suites
sanityTestSuite=unittest.TestSuite([tc1,tc2])
functionalTestSuite=unittest.TestSuite([tc3,tc4])
MasterTestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(MasterTestsuite)
