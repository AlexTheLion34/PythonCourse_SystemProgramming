from least_square_method.FillTable import FillTable
from least_square_method.MakeGraph import MakeGraph
from restoring_data.MakeTable import MakeTable
from restoring_data.Vinification import Vinification


class Test:

    @staticmethod
    def test():
        print("Аппроксимация")
        print("------------")
        ft = FillTable()
        ft.fill_table()
        mg = MakeGraph()
        mg.make_graph()
        print("------------")
        print("Восстановление данных")
        mt = MakeTable()
        mt.put_matrix_in_table()
        v = Vinification()
        v.receive_data()


Test.test()
