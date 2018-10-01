# Swift

### Contents

+ #### [Data Type](#Swift_Data_Type)
+ #### [JSON](#Swift_JSON)
+ #### [UI Attributes](#Swift_UIAttributes)
	+ ##### [UITabBar](#Swift_UITabBar])
		+ ###### tintColor
		+ ###### barTintColor
		+ ###### backgroundColor
+ #### [Permission](#Swift_Permission)
	+ ##### [Http Request](#Swift_Permission_HttpRequest)
	+ ##### [Camera](#Swift_Permission_Camera)
	+ ##### [Microphone](#Swift_Permission_Microphone)
	+ ##### [Photo Album](#Swift_Permission_PhotoAlbum)
	+ ##### [Location](#Swift_Permission_Location)



<a name='Swift_Data_Type' />

### Data Type


<a name = "Swift_UIAttributes">

## UI Attributes


<a name = "Swift_UITabBar" />

### Custom UITabBar tintColor & barTintColor & backgroundColor Swift_UITabBar


#### Entire UITabbar, code @ Appdelegate.swift

##### tintColor
```swift
UITabBar.appearance().tintColor = UIColor.white
```

##### barTintColor
```swift
UITabBar.appearance().barTintColor = UIColor.white
```

##### backgroundColor
```swift
UITabBar.appearance().backgroundColor = UIColor.white
```


#### Specific ViewController UITabbar, code @ ViewController.swift

##### tintColor
```swift
self.tabBarController?.tabBatbar.TintColor = UIColor.white
```

##### barTintColor
```swift
self.tabBarController?.tabBatbar.barTintColor = UIColor.white
```

##### backgroundColor
```swift
self.tabBarController?.tabBatbar.backgroundColor = UIColor.white
```



<a name="Swift_UIWebView" />

### UIWebView

#### Make UIWebView support `http`

+ Method 1
	- Right Click on `info.plist`
	- Select `Open As` > `Source Code`
	- Copy & Paste

		```swift
		<key>NSAppTransportSecurity</key>
		<dict>
    		<key>NSAllowsArbitraryLoads</key>
    		<true/>
    	</dict>
		```

+ Method 2
	- Select `info.plist`
	- Right Click & Choose `Add Row`
	- Select `App Transport Sercurity Settings`
	- Click the arrow to make it down as a Dictionary
	- Press `+` & Choose `Allow Arbitary Loads`
	- Set the boolean value from default NO to `YES`



<a name= "Swift_JSON" />

### JSON

+ Under Development



<a name = "Swift_Permission" />

### Permission
#### When developing in Swift, we often use some hardware devices.  
#### We should set up the permission in the `info.plist` file
> Right click on `info.plist` & select `Open As` > `Source Code`


<a name = "Swift_Permission_HttpRequest" />

+ ##### Http Request

```swift
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
</dict>
```



<a name = "Swift_Permission_Camera" />

+ ##### Camera

```swift
<key>NSCameraUsageDescription</key>
<string>Allow to access camera</string>
```


<a name = "Swift_Permission_Microphone" />

+ ##### Microphone

```swift
<key>NSMicrophoneUsageDescription</key>
<string>Allow to access microphone</string>
```


<a name =  "Swift_Permission_PhotoAlbum" />

+ ##### Photo Album(#Swift_Permission_PhotoAlbum)


```swift
<key>NSPhotoLibraryAddUsageDescription</key>
<string>Allow to add media into photo album</string>
<key>NSPhotolibraryusageDescription</key>
<string>Allow to access photo album</string>
```


<a name =  "Swift_Permission_Location" />

+ ##### Location(#Swift_Permission_Location)

```swift
<key>NSLocationAlwaysUsageDescription</key>
<string>Allow to access user location</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>Allow to access user location</string>
```