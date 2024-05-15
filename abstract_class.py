from abc import ABC, abstractmethod

# Abstract Class = Interface (di bahasa lain)


# Abstraksi Integration -> Contract / Interface / Abstract Class
# Abstract Class = Class tanpa logic, hanya contract
# (hanya method aja (nama method, parameter method, return method))
class BaseIntegration(ABC):

    @abstractmethod
    def create_order(self):  # Type Hinting (return dari create_order itu str)
        pass

    @abstractmethod
    def delete_order(self):
        pass


def createOrder(integration: BaseIntegration):
    # Tidak peduli integration itu pakai shopee, tokopedia, dll.
    # Artinya bisa dipakai Tokopedia, Shopee, selama pakai abstraksi BaseIntegration
    return integration.create_order()

###################################################################


class TokopediaIntegration(BaseIntegration):

    def create_order(self):  # ini kontrak dari BaseIntegration, harus dibikin logicnya
        return 'tokopedia create order'

    def create_order_2(self):
        return 'tokopedia create order 2'


class ShopeeIntegration(BaseIntegration):

    def create_order(self):
        return 'shopee create order'


shopeeIntegration = ShopeeIntegration()
tokopediaIntegration = TokopediaIntegration()

print(tokopediaIntegration.create_order_2())
# order = createOrder(tokopediaIntegration)
# print(order)
