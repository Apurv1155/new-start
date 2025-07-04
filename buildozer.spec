[app]
title = FaceApp
package.name = faceapp
package.domain = org.digitalapurv
source.include_exts = py,xml,jpg,png,kv,ini,dat,json,txt
requirements = python3,kivy,flask,flask-cors,opencv-python-headless,numpy,requests
android.permissions = INTERNET, CAMERA, WAKE_LOCK
android.ndk_extra_flags = -DOPENCV_ANDROID_SKIP_PNG=ON
android.add_src = assets
