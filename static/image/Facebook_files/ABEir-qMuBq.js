if (self.CavalryLogger) { CavalryLogger.start_js(["oO6Ic"]); }

__d("FriendingCometFriendRequestsRootQuery$Parameters",[],(function(a,b,c,d,e,f){"use strict";a={kind:"PreloadableConcreteRequest",params:{id:"3356705357724019",metadata:{},name:"FriendingCometFriendRequestsRootQuery",operationKind:"query",text:null}};e.exports=a}),null);
__d("FriendingCometFriendRequestsRoot.entrypoint",["FriendingCometFriendRequestsRootQuery$Parameters","JSResourceForInteraction","ProfileCometTimelineListViewRouteRoot.entrypoint","WebPixelRatio"],(function(a,b,c,d,e,f){"use strict";a={getPreloadProps:function(a){var c={scale:b("WebPixelRatio").get()},d=a.routeProps,e=d.profileID;d=d.viewerID;e=e!=null&&d!=null?{entryPoint:b("ProfileCometTimelineListViewRouteRoot.entrypoint"),entryPointParams:{routeProps:{userID:a.routeProps.profileID,viewerID:a.routeProps.viewerID}}}:void 0;return{entryPoints:{profileEntryPoint:e},queries:{friendingCometFriendRequestsRootQueryReference:{parameters:b("FriendingCometFriendRequestsRootQuery$Parameters"),variables:c}}}},root:b("JSResourceForInteraction")("FriendingCometFriendRequestsRoot.react").__setRef("FriendingCometFriendRequestsRoot.entrypoint")};e.exports=a}),null);