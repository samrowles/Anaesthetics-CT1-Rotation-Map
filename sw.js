/**
 * Legacy Service Worker Cleanup Stub
 * Clears obsolete caches for this retired path and unregisters itself.
 */
self.addEventListener('install', () => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  const keep = [];
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys
          .filter((k) => k.startsWith('ct1-') && !keep.includes(k))
          .map((k) => caches.delete(k))
      ))
      .then(() => self.registration.unregister())
      .then(() => self.clients.claim())
      .catch(() => {})
  );
});
