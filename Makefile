all: build/oppressive.request.js build/oppressive.offline.js build/oppressive.online.js build/oppressive.app.js


build/oppressive.request.js: oppressive.js request.oppressive.js
	java -jar compiler.jar --js oppressive.js request.oppressive.js > build/oppressive.request.js

build/oppressive.offline.js: oppressive.js offline.oppressive.js
	java -jar compiler.jar --js oppressive.js offline.oppressive.js > build/oppressive.offline.js

build/oppressive.online.js: oppressive.js online.oppressive.js
	java -jar compiler.jar --js oppressive.js online.oppressive.js > build/oppressive.online.js

build/oppressive.app.js: oppressive.js app.oppressive.js
	java -jar compiler.jar --js oppressive.js app.oppressive.js > build/oppressive.app.js
