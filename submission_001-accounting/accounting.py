from user import authentication
from transactions import journal
import banking
# from banking.fvb import reconciliation as fvb
import sys




if __name__ == "__main__":
    if len(sys.argv) >= 2:
        a = sys.argv[1:]
        for word in a:
            print(word.strip())
    authentication.authenticate_user()
    journal.receive_income(100)
    journal.pay_expense(100)
    banking.do_reconciliation()


    