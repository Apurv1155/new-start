[app]
title = FaceApp
package.name = faceapp
package.domain = org.digitalapurv
source.dir = .             # <— this is required
version = 1.0.0            # <— version is required
requirements = python3,kivy,flask,flask-cors,opencv-python-headless,numpy,requests
source.include_exts = py,xml,jpg,png,kv,ini,dat,json,txt
android.permissions = INTERNET, CAMERA, WAKE_LOCK
android.ndk_extra_flags = -DOPENCV_ANDROID_SKIP_PNG=ON
android.add_src = assets
