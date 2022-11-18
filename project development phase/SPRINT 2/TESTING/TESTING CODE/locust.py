from locust import HttpUser, task

class WebsiteUser(HttpUser): 
    
    @task 
    def index(self): 
        self.client.get(url='/')
    @task 
    def task1(self): 
        self.client.get(url='/login') 
    
    @task 
    def task2(self): 
        self.client.get(url='/openaddcategory')

    @task 
    def task3(self): 
        self.client.get(url='/addcat')

    @task 
    def task4(self): 
        self.client.get(url='/opendelcategory')

    @task 
    def task5(self): 
        self.client.get(url='/delcat')

    @task 
    def task6(self): 
        self.client.get(url='/openupcategory')

    @task 
    def task7(self): 
        self.client.get(url='/upcat')

    @task 
    def task8(self): 
        self.client.get(url='/openviewcategory')


    @task 
    def task9(self): 
        self.client.get(url='/openaddpro')

    @task 
    def task10(self): 
        self.client.get(url='/openaddpro')

    @task 
    def task11(self): 
        self.client.get(url='/addpro')

    @task 
    def task12(self): 
        self.client.get(url='/opendelpro')

    @task 
    def task13(self): 
        self.client.get(url='/delpro')

    @task 
    def task14(self): 
        self.client.get(url='/openuppro')

    @task 
    def task15(self): 
        self.client.get(url='/uppro')

    @task 
    def task16(self): 
        self.client.get(url='/openviewcat')
    
    @task 
    def task17(self): 
        self.client.get(url='/opendelorder')

    @task 
    def task18(self): 
        self.client.get(url='/mkdelorder')

    @task 
    def task19(self): 
        self.client.get(url='/openviewpro')
    
    @task 
    def task20(self): 
        self.client.get(url='/openviewpurchase')
    
    @task 
    def task21(self): 
        self.client.get(url='/openviewsummary')