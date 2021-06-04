import math
import random
import time
import pygame
from pygame import mixer

# pygame'yi başlatır
pygame.init()
#yükseklik ve genişlik belirlendi
display_width=800
display_height= 600
# ekranı oluşturur
screen = pygame.display.set_mode((800, 600))
#program ikonunu değiştirir.
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#arka planı ve başlığı tanımladım
pygame.display.set_caption("Space Invader")
background = pygame.image.load('background1.jpg')
running = True
menuu = True
#renkler
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red=(200,0,0)
bright_green=(50,205,50)
green= (0,128,0)

def text_objects(text, font):#yazıları yazdırır
    textSurface = font.render(text, True, black)#ekrana bastırır
    return textSurface, textSurface.get_rect()
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))#skor için değişken tanımladım
    screen.blit(score, (x, y))#ekrana bastırır x,y 'ye göre


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))#show score ile aynı mantık
    screen.blit(over_text, (200, 250))

def win_text():#show score ile aynı mantık
    over_text = over_font.render("Bölümü geçtin", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):#oyuncuyu ekrana bastırır
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):#düşmanı ekrana bastırır
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):#mermiyi ekrana bastırır
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):#trigonometrik üçgen hesaplaması ile belirttiğimiz sınırlarda çarpısma tespit eder
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#menu
def button(msg,x,y,w,h,ic,ac,action=None):#button oluşturma kodu
    global menuu
    mouse = pygame.mouse.get_pos() #mouse ve tıklama verisini tutar
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:#eğer butonumuz üstünde mouse imleçi geldiyse açık renk yapar butonu
        pygame.draw.rect(screen, ac,(x,y,w,h))#ekrana bastırır

        if click[0] == 1 and action != None:#tıklama olursada action parametresine göre çalıştırır
            #print(action)
            action()


    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))#diğer türlü buton aynı renk kalır

    smallText = pygame.font.SysFont("comicsansms",20)#text fontu tanımladık
    textSurf, textRect = text_objects(msg, smallText)#text boyutu ve text tanımlanır
    textRect.center = ( (x+(w/2)), (y+(h/2)) )#merkeze göre konumu ayarlanır
    screen.blit(textSurf, textRect)

def quitgame():
        quit()#oyundan çıkış yapar


def howtoPlay():#nasıl yapılır menusu
    icon = pygame.image.load('ufo.png')#icon bastırır
    pygame.display.set_icon(icon)
    global how#değişkenlerimiz global çünkü fonksiyon dışındada kullanmak istiyoruz
    global menuu
    menuu=False#how menusu açıldığında menuyu kapatır
    how=True
    running =False#açık oyun varsa kapatır
    while how:#how menusu açık olduğu sürece çalışır
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)#ekranı beyaz yapar
        screen.blit(background, (0, -100))#background olarak tanımladığım ekranı -100 kadar y ekseninde kaydırır
        largeText = pygame.font.SysFont("comicsansms",115)#font belirler
        smallText = pygame.font.SysFont("comicsansms",23)
        TextSurf, TextRect = text_objects("Nasıl oynanır:", largeText)
        TextSurf1, TextRect1 = text_objects("* Ok tuşları ile gemiyi sağa sola hareket ettir!", smallText)#yazacağımız yazıyı font ile gireriz
        TextSurf3, TextRect3 = text_objects("*100 skora ulaşarak bölüm geç veya survival modunda en iyi skorunu yap!", smallText)
        TextSurf2, TextRect2 = text_objects("*düşmanın kırmızı bölgeye ulaşmasına izin verme!", smallText)
        TextRect.center = ((display_width/2),(display_height/5))#merkez egöre konumunu hesaplarız
        TextRect1.center = ((display_width/2),(display_height/2.8))
        TextRect2.center = ((display_width/2),(display_height/2.4))
        TextRect3.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)#ekrana yazdırır
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf3, TextRect3)

        button("Menu",350,400,100,50,green,bright_green,menu)#butonumuz menuyü açar

        pygame.display.update()#ekrandaki nesnelerin güncellenmesini sağlar

def yapimcilar():
    global how
    global menuu
    menuu=False
    how=True
    while how:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)#
        screen.blit(background, (0, -100))#
        smallText = pygame.font.SysFont("comicsansms",23)#
        largeText = pygame.font.SysFont("comicsansms",115)#
        TextSurf, TextRect = text_objects("yapımcılar:", largeText)#
        TextSurf2, TextRect2 = text_objects("*Senin ismin!", smallText)#
        TextRect2.center = ((display_width/2),(display_height/2.4))#
        TextRect.center = ((display_width/2),(display_height/5))#
        screen.blit(TextSurf2, TextRect2)#
        screen.blit(TextSurf, TextRect)#
        button("Menu",350,450,100,50,green,bright_green,menu)#buraları howtoplay kısmında anlattım

        pygame.display.update()
def menu():
    global how
    global menuu
    global background
    global running
    menuu=True
    how=False
    running =False
    print("menu",menuu)
    while menuu:#
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)#

        screen.blit(background, (0, -100))#
        largeText = pygame.font.SysFont("comicsansms",115)#
        TextSurf, TextRect = text_objects("Menu", largeText)#
        TextRect.center = ((display_width/2),(display_height/4))#buraları howtoplay kısmında anlattım
        screen.blit(TextSurf, TextRect)#

        button("Normal",150,350,100,50,green,bright_green,game_loop)#en son parametre çağırmak istediğimiz fonksiyon
        button("Hayatta kalma!",150,430,100,50,green,bright_green,game_loop2)#
        button("Çıkış",550,350,100,50,red,bright_red,quitgame)#
        button("Nasıl oynanır ?",288,350,100,50,green,bright_green,howtoPlay)##
        button("Yapımcılar",421,350,100,50,green,bright_green,yapimcilar)#

        pygame.display.update()##buraları howtoplay kısmında anlattım

# Game Loop

def game_loop():

    global running
    global playerX#global olarak veri tanıtıyorum ki fonksiyon dışındanda  çağırıp değişebilsin
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state
    global score_value
    global playerImg
    global menuu
    global enemyImg
    global font
    global bulletImg
    global over_font
    global background
    # Background


    # Sound
    mixer.music.load("background.wav")#seçtiğim mevcut wav dosyasının ismini girip oynat dedim
    mixer.music.play(-1)#-1 olarak ayarladım çünkü müzik bittikten sonra yeniden başlamasını istiyorum

    # ikon resmini belirledim
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('player.png')#oyuncu resmi yüklendi
    playerX = 370#playerin başlayacağı konum(x)
    playerY = 480#playerin başlayacağı konum(y)
    playerX_change = 0#playerin x ekseninde hareket hızı en başta sıfır daha sonra değişecek

    # Enemy
    enemyImg = [] #her bir düşmana değişiklik uygulamak için dizi olarak oluşturdum bunları düşman resmi
    enemyX = [] #düşmanın x kordinati
    enemyY = []#düşmanın y kordinati
    enemyX_change = []#düşmanın x ekseninde ilerleme hızı
    enemyY_change = []#düşmanın y ekseninde ilerleme hızı
    num_of_enemies = 18#mevcut bolümdeki düşmanın sayısı

    for i in range(num_of_enemies):#her bir düşmana değişiklik uygulamak için for kullanıyorum
        enemyImg.append(pygame.image.load('enemy.png'))#düşman sayısı kadar resim bastırıyor ekrana
        enemyX.append(random.randint(0, 736)) #belirtilen parametreler arası x ekseninde random olarak düşman beliriyor
        enemyY.append(random.randint(50, 150))#belirtilen parametreler arası y ekseninde random olarak düşman beliriyor
        enemyX_change.append(1)#düşmanın x ekseninde ilerleme hızı 1'e eşitlendi
        enemyY_change.append(40)#düşmanın y ekseninde ilerleme hızı 40'a eşitlendi

    # mermi

    # hazır - mermiyi ekranda göremezsin
    # ateş - mermi hareket etmeye başlar

    bulletImg = pygame.image.load('bullet.png')#mermi resmi
    bulletX = 0#
    bulletY = 480#
    bulletX_change = 0#
    bulletY_change = 10#açıklandı yukarda
    bullet_state = "ready"#merminin mantıksal durumu hazır olarak belirtildi

    # Score

    score_value = 0#mevcut skoru tutan değer
    font = pygame.font.Font('freesansbold.ttf', 32)#font

    textX = 10#skorun ekranda belireceği x kordinatı
    testY = 10#skorun ekranda belireceği y kordinatı

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    running=True

    while running:#running true olduğu sürece oyun devam edecek

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # oyuncu gemisinin klavye kontrolu için gereken kısmı
            if event.type == pygame.KEYDOWN:# herhangi bir tuşa basıldığında girer
                if event.key == pygame.K_LEFT:#sol çalışırsa gidiş yonu -2 olur
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:#sağ çalışırsa gidiş yonu 2 olur
                    playerX_change = 2
                if event.key == pygame.K_SPACE:#space çalışırsa
                    if bullet_state is "ready":#mermi eğer ateşlenmemişse ateşler
                        bulletSound = mixer.Sound("laser.wav")#ses dosyasını çalıştırır
                        bulletSound.play()#oynatır
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX+25#merminin çıkış kordinatı
                        fire_bullet(bulletX, bulletY)#kordinatları verilen mermi bu fonksiyonla yola çıkıyor

            if event.type == pygame.KEYUP:#tuş basıldıktan sonraki durumda çalışır
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0#tuş basıldıktan sonra çekildiyse geminin durması sağlanır



        playerX += playerX_change#oyuncunun mevcut hareket hızına göre her framede pozisyonu değişir
        if playerX <= 0:#oyuncu konumu sıfırsa ekran sınırını aşmaması için 0 da sabitlenir
            playerX = 0
        elif playerX >= 736:#bu da y ekseni için
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):#her bir düşmana değişiklik uygulamak için for kullanıyorum

            # Game Over
            if enemyY[i] > 440 and score_value<100:#eğer kullanıcı skoru geçemediyse ve düşmanlardan herhangi birisi belirlenen ekran sınırı olan 440'ı geçerse oyun biter
                for j in range(num_of_enemies):#her bir düşmanın pozisyonunu görmek için for kullanıyorum
                    enemyY[j] = 2000#game over olduysa düşmanı haritadan uzaklaştırır
                game_over_text()#game over yazdıran fonksiyonu çağırır
                button("Menu",350,450,100,50,green,bright_green,menu)
                button("Tekrar Oyna",150,450,100,50,green,bright_green,game_loop)#3 adet buton menu çıkış  ve sonraki level için
                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True
                #menu()
                #break

            enemyX[i] += enemyX_change[i]#düşmanın mevcut hareket hızına göre her framede pozisyonu değişir
            if enemyX[i] <= 0:
                enemyX_change[i] = 1#düşman hızı 0 ise default olarak bire cevirir
                enemyY[i] += enemyY_change[i]#ve sağ kenara vardığında aşağı belirtilen miktarda kayar
            elif enemyX[i] >= 736:#düşman soldaki ekran sınırına ulaştığında sola doğru gitmesi gerektiğinden 1den -1 olur gidiş hızı
                enemyX_change[i] = -1
                enemyY[i] += enemyY_change[i]#ve sol kenara vardığında aşağı belirtilen miktarda kayar

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)#çarpışma tepiti için her bir düşmanın x,y ve merminin x,y kordinatları alınıp karşılaştırılır
            if collision:#çarpışma varsa
                explosionSound = mixer.Sound("explosion.wav")#patlama sesi
                explosionSound.play()#oynatılır
                bulletY = 480 #mermi playerin y seviyesine geri döner
                bullet_state = "ready"#durum hazır olarak tekrar değiştirilir
                score_value += 1#düşman gemisi vurulduğu için sore bir artırılır
                enemyX[i] = random.randint(0, 736)#ve düşman belirtilen ekran kordinatlarından bir daha doğar
                enemyY[i] = random.randint(0, 50)#
            enemy(enemyX[i], enemyY[i], i)#düşmanı yeniden konumlandırması için fonksiyona parametreleri gönderdik
            if score_value >= 100:#kazanma durumu : eğer skor istenen seviyeye gelirse oyun kazanılmış olur
                for j in range(num_of_enemies):
                    enemyY[j] = 2000#oyun kazanıldığında ekrandaki düşmanlar 2000 y seviyesine gönderilir
                win_text()#kazandın textini aktif eder
                button("Menu",350,450,100,50,green,bright_green,menu)#butonlar
                button("2. Bölüm",150,450,100,50,green,bright_green,game_loop2lvl)#
                button("çık",550,450,100,50,red,bright_red,quitgame)#

        # Mermi hareketi
        if bulletY <= 0:#mermi olurda y ekseninde 0  da veya negatifde ise oyuncu gemisinin seviyesi 480'e eşitlenir
            bulletY = 480
            bullet_state = "ready"#durum default olarak hazır olur

        if bullet_state is "fire":#mermi state'i ateşlendi ise ateşleme fonksiyonuna gönderir mevcut kordinatlarla
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change#ve mermi yukarı gitmesi gerekiği için bullety den çıkarıyoruz eklersek aşağı iner

        player(playerX, playerY)#oyuncumuzunda yerini tekrar güncellemek adına değişiklik yapılan kordinatların son halini göderir
        show_score(textX, testY)#skoru göstermek için kordinatları alır ve fonksiyona gönderir.
        pygame.display.update()#nesnelerin değişiklikleri görünmesi için sayfayı devamlı yeniler

def game_loop2lvl():#game_loop gibi tek farkı  2. level için görsel ve oynanış için parametreler değişti

    global running
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state
    global score_value
    global playerImg
    global menuu
    global enemyImg
    global font
    global bulletImg
    global over_font
    global background
    # Background


    # Sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 25

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('enemy1.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)
        enemyY_change.append(40)



    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # Score

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    testY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    running=True
    print(running)
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX+25
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440 and score_value<125:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                button("Menu",350,450,100,50,green,bright_green,menu)
                button("Tekrar Oyna",150,450,100,50,green,bright_green,game_loop2lvl)
                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True
                #menu()
                #break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 1
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -1
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)

            enemy(enemyX[i], enemyY[i], i)
            if score_value >= 125:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                win_text()
                button("Menu",350,450,100,50,green,bright_green,menu)
                button("3. Bölüm",150,450,100,50,green,bright_green,game_loop3lvl)
                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True
                #menu()
                #break
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()


def game_loop3lvl():#game_loop gibi tek farkı  3. level için görsel ve oynanış için parametreler değişti

    global running
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state
    global score_value
    global playerImg
    global menuu
    global enemyImg
    global font
    global bulletImg
    global over_font
    global background
    # Background


    # Sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 25

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('enemy2.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)
        enemyY_change.append(40)

    # Bullet

    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving

    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # Score

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    testY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    running=True
    print(running)
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX+25
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440 and score_value<150:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                button("Menu",350,450,100,50,green,bright_green,menu)
                button("Tekrar Oyna",150,450,100,50,green,bright_green,game_loop3lvl)
                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True
                #menu()
                #break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 1
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -1
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)

            enemy(enemyX[i], enemyY[i], i)
            if score_value >= 150:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                over_text = over_font.render("Oyunu Bitirdin!!", True, (255, 255, 255))
                screen.blit(over_text, (200, 250))
                button("Menu",350,450,100,50,green,bright_green,menu)

                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True
                #menu()
                #break
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()


def game_loop2():#game_loop gibi tek farkı  hayatta kalma modu olarak görsel ve oynanış için parametreler değişti skor ile kazanmak iptal edildi amaç oyuncunun en cok skoru yapabilmesi

    global running
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global bullet_state
    global score_value
    global playerImg
    global menuu
    global enemyImg
    global font
    global bulletImg
    global over_font
    global background
    # Background

    #score
    score_value = 0
    # Sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 25

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('enemy1.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)
        enemyY_change.append(40)

    # Bullet

    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving

    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # Score


    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    testY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    running=True
    print(running)
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX+25
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440 :
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()

                button("Tekrar Oyna",150,450,100,50,green,bright_green,game_loop2)
                button("Menu",350,450,100,50,green,bright_green,menu)
                button("çık",550,450,100,50,red,bright_red,quitgame)
                menuu =True


            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]
            #burada yeni bir if şartı yazıp score>100'den oyunu kazanndır demediğim için oyun sonsuz oldu ve oyun modu kullanıcının her seferinde daha iyi skor sağlaması için değiştirildi
            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()

menu()#menu'yu çağırdım ki kullanıcı giriş yaptığında ilk olarak menu ile karşılaşsın.

