<?php

interface RestaurantInterface
{
        public function  acceptOnlineOrder();
        public function  payOnline();
        public function  walkInCustomerOrder();
        public function  payInPerson();

}

class OnlineClient implements RestaurantInterface
{
        public function  acceptOnlineOrder()
        {
            // placing online order .......
        }

        public function  payOnline()
        {
            //paying online ......
        }
}

?>