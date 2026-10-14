/* ============================================================
   부산자동차마이스터고 취업지원부 · 면접 복기 아카이브
   공통 모션 스크립트 — "Deep Glass" v2.0
   모든 페이지 </body> 직전에 <script src="motion.js" defer></script> 로 연결
   - 스크롤 리빌(toss 스타일 순차 등장)
   - 카드 커서 스포트라이트
   - JS 없거나 실패해도 콘텐츠는 항상 보임 (progressive enhancement)
   ============================================================ */
(function () {
    "use strict";

    var reduceMotion = window.matchMedia &&
        window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    document.documentElement.classList.add("js");

    /* ---------- 1. 스크롤 리빌 ---------- */
    var REVEAL_SELECTOR = [
        ".hero", ".page-head", ".container > header",
        ".list-card", ".qa-card", ".panel", ".interview-room-section",
        ".tip-box", ".score-board", ".room-block", ".category-title"
    ].join(", ");

    function setupReveal() {
        var targets = document.querySelectorAll(REVEAL_SELECTOR);
        if (!targets.length) return;

        if (reduceMotion || !("IntersectionObserver" in window)) {
            targets.forEach(function (el) { el.classList.add("reveal", "in-view"); });
            return;
        }

        // 같은 부모 안에서의 순서에 따라 살짝 다른 딜레이 (stagger)
        var parentCounters = new WeakMap();
        targets.forEach(function (el) {
            el.classList.add("reveal");
            var parent = el.parentElement;
            var idx = parentCounters.get(parent) || 0;
            el.style.transitionDelay = Math.min(idx, 8) * 70 + "ms";
            parentCounters.set(parent, idx + 1);
        });

        var io = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("in-view");
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });

        targets.forEach(function (el) { io.observe(el); });
    }

    /* ---------- 2. 카드 커서 스포트라이트 (list-card) ---------- */
    function setupSpotlight() {
        if (reduceMotion) return;
        var cards = document.querySelectorAll(".list-card");
        cards.forEach(function (card) {
            card.addEventListener("pointermove", function (e) {
                var rect = card.getBoundingClientRect();
                var x = ((e.clientX - rect.left) / rect.width) * 100;
                var y = ((e.clientY - rect.top) / rect.height) * 100;
                card.style.setProperty("--mx", x + "%");
                card.style.setProperty("--my", y + "%");
            });
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            setupReveal();
            setupSpotlight();
        });
    } else {
        setupReveal();
        setupSpotlight();
    }
})();
