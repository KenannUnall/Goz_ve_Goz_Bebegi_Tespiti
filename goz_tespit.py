import cv2
import time

eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye.xml") # Önceden eğitilmiş modeli dahil ediyoruz.

cap = cv2.VideoCapture(0)    # Ana kameramız üzerinde çalışma yapacağımız belirtiyoruz

while cap.isOpened():

    ret,img = cap.read()
    img = cv2.flip(img, 2)      # Alınan görüntüyü y ekseninde döndürme

    if ret==False:
        time.sleep(20)
        break

    img=cv2.resize(img,(1280,720))      # Alınan görüntüyü istenilen boyuta göre ayarlama

    #img = cv2.imread(r"photos/1588088785877.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # Resmi gri formata çevirme işlemi. Tek kanala düşürme .

    threshold=0

    eyes = eye_cascade.detectMultiScale(gray, 1.34, 9)  # Göz alanlarının tespiti

    eyes = eyes[:2] # Göz olarak tespit edilen nesnelerin ilk 2 değerinin alınması.

    for(x,y,w,h) in eyes:

        cv2.rectangle(img,(x,y+15),(x+w,y+h-15),(0,0,255),2) # tespit edilen nesneleri rectangle ile işaretleme
        roi = img[y+15: y+h-15, x:x+w] # Göz bebeği tespiti için çalışma alanımızı tespit edilen göz alanında yapmak için
        #Böylecelikle başarı oranı daha da artmaktadır .
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0) #Ani piksel değişikliğinden dolayı tespiti zorlaştıran piksel değerlerinin yumuşaltılma işlemi.
        _, threshold = cv2.threshold(gray_roi,50, 255, cv2.THRESH_BINARY_INV) # Bu kısımında resimdeki piksel değerleri 50 den büyük ise 0 değeri olacak
        # değilse 255 değeri atasnacak.
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # bu kısımda gözbebeğinin kontürleri alınacak.
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) # Alanlara göre sıralanma işlemi yapılacak.
        print(contours)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt) # Contourun kordinat bilgisi alınması
            print(x, y,w,h)
         
            # cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2) # En büyük alanlı nesne göz bebeği olarak kabul edilip rectangle ile tespiti gösterme işlemi yapılcaktır.

            break # Tek bir contour için yapılması gerektiği için

    cv2.imshow('img',img)
    cv2.imshow("thres",threshold)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()