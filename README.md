
# Göz Tespiti ve Göz Bebeği İzleme Uygulaması

Bu proje, OpenCV kütüphanesi kullanarak bir video kaynağında göz tespiti ve göz bebeği izleme işlemi gerçekleştirir. Uygulama, bilgisayarın ön kamerasından alınan görüntülerde gözleri ve gözbebeklerini tespit etmek için Haarcascades sınıflandırıcı modelini kullanır.

## Özellikler

- Bilgisayarın ön kamerası ile gerçek zamanlı göz tespiti yapılır.
- Göz tespit edilen bölgelerde, gözler dikdörtgenlerle işaretlenir.
- Göz bebeği tespiti yapılır ve en büyük kontürler göz bebeği olarak kabul edilir.
- Gerçek zamanlı işlemle birlikte her iki göz de takip edilebilir.

## Kullanım

1. **Python ve gerekli kütüphaneleri yükleyin:**

   ```bash
   pip install opencv-python
   ```

2. **Haarscascade Göz Modeli Dosyasını Edinin:**

   Bu projede, `haarcascade_eye.xml` adlı bir önceden eğitilmiş model kullanılır. Bu dosyayı [buradan indirebilirsiniz](https://github.com/opencv/opencv/tree/master/data/haarcascades).

3. **Kodunuzu Çalıştırın:**

   Uygulamayı çalıştırmak için terminal veya komut satırından aşağıdaki komutu kullanın:

   ```bash
   python eye_tracking.py
   ```

4. **Çalıştırma ve Sonuçlar:**

   Uygulama, ön kameranızı başlatacak ve kamerada tespit edilen gözleri kırmızı dikdörtgenlerle işaretleyecektir. Göz bebeği tespiti de mavi dikdörtgenlerle gösterilecektir. Programdan çıkmak için 'q' tuşuna basabilirsiniz.

## Açıklama

- **Göz Tespiti:** Haarcascades sınıflandırıcıları ile göz tespiti yapılır.
- **Göz Bebeği Tespiti:** Görüntüdeki gözlerin iç kısmındaki en büyük kontür (göz bebeği) tespit edilir ve mavi dikdörtgenle işaretlenir.
- **Ekran Boyutu:** Görüntüler 1280x720 piksel boyutlarına ayarlanır.

## Kodun Açıklaması

1. **Video Kaynağı:** `cv2.VideoCapture(0)` ile bilgisayarın ön kamerası kullanılır.
2. **Göz Algılama:** `CascadeClassifier` ile gözlerin yerleri tespit edilir.
3. **Göz Bebeği Algılama:** Tespit edilen gözlerin içinde en büyük kontür bulunur ve göz bebeği olarak kabul edilir.
4. **Görüntü İşleme:** Tespit edilen gözler ve gözbebekleri, dikdörtgenler ile işaretlenir ve görüntü üzerinde gösterilir.

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi
- Haarcascades Göz Tespit Modeli
