import os

# // bitheart, created by daniel

SYSTEM = ('Bitheart')

setupFiles = ['data.txt', 'admin']
setupDirs = ['Client']

def setup():
    if os.path.exists(SYSTEM):
        dir = os.listdir(SYSTEM)
        if all(file in dir for file in setupFiles + setupDirs):
            handler()
        else:
            print('❌ File is missing')
    else:
        os.makedirs(SYSTEM) # Creates our system
        for dir in setupDirs:
            os.makedirs(f'{SYSTEM}/{dir}')
            print(f'📂 Downloaded dir [{dir}]')

        for file in setupFiles:
            with open(f'{SYSTEM}/{file}', 'a'):
                print(f'✅ Downloaded file [{file}]')

def handler():
    print('👋 Welcome,')
    while True:
        run = input('💗: ') # // Our command handler!
        if run.startswith('create'):
            fileName = str(run.split()[1])
            Content = input('[💗] Content: ')

            with open(f'{SYSTEM}/Client/{fileName}', 'w') as file:
                file.write(Content)
              
setup() 
