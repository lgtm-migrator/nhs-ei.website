!function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=2)}([function(e,t){NodeList.prototype.forEach||(NodeList.prototype.forEach=Array.prototype.forEach),Array.prototype.includes||Object.defineProperty(Array.prototype,"includes",{enumerable:!1,value:function(e){return this.filter((function(t){return t===e})).length>0}}),Element.prototype.matches||(Element.prototype.matches=Element.prototype.msMatchesSelector||Element.prototype.webkitMatchesSelector),Element.prototype.closest||(Element.prototype.closest=function(e){var t=this;do{if(Element.prototype.matches.call(t,e))return t;t=t.parentElement||t.parentNode}while(null!==t&&1===t.nodeType);return null})},function(e,t){if(document.querySelector(".nhsuk-header__search")){var n=document.querySelector("#toggle-search"),r=document.querySelector("#close-search"),o=document.querySelector("#wrap-search"),i=document.querySelector("#content-header");n.addEventListener("click",(function(){n.setAttribute("aria-expanded",!0),n.classList.add("is-active"),o.classList.add("js-show"),i.classList.add("js-show")})),r.addEventListener("click",(function(){n.removeAttribute("aria-expanded"),n.classList.remove("is-active"),o.classList.remove("js-show"),i.classList.remove("js-show")}))}},function(e,t,n){"use strict";n.r(t);var r=function(e,t){if(e&&t){var n="true"===e.getAttribute(t)?"false":"true";e.setAttribute(t,n)}},o=function(e,t){if(e&&t){var n=e.getAttribute("aria-controls");if(n){var o=document.getElementById(n);o&&(o.classList.toggle(t),r(e,"aria-expanded"))}}},i=function(){var e="boolean"==typeof document.createElement("details").open,t=document.querySelectorAll("details");t.length&&t.forEach((function(t,n){t.hasAttribute("nhsuk-polyfilled")||function(t,n){t.setAttribute("nhsuk-polyfilled","true"),t.id||t.setAttribute("id","nhsuk-details".concat(n));var o=document.querySelector("#".concat(t.id," .nhsuk-details__text"));o.id||o.setAttribute("id","nhsuk-details__text".concat(n));var i=document.querySelector("#".concat(t.id," .nhsuk-details__summary"));i.setAttribute("role","button"),i.setAttribute("aria-controls",o.id),i.setAttribute("tabIndex","0"),!0===(null!==t.getAttribute("open"))?(i.setAttribute("aria-expanded","true"),o.setAttribute("aria-hidden","false")):(i.setAttribute("aria-expanded","false"),o.setAttribute("aria-hidden","true"),e||(o.style.display="none"));i.addEventListener("click",(function(){r(i,"aria-expanded"),r(o,"aria-hidden"),e||(o.style.display="true"===o.getAttribute("aria-hidden")?"none":"",t.hasAttribute("open")?t.removeAttribute("open"):t.setAttribute("open","open"))})),i.addEventListener("keydown",(function(e){13!==e.keyCode&&32!==e.keyCode||(e.preventDefault(),i.click())}))}(t,n)}))};function c(e){if("A"!==e.tagName||!1===e.href)return!1;var t=document.querySelector(e.hash);if(!t)return!1;var n=function(e){var t=e.closest("fieldset");if(t){var n=t.getElementsByTagName("legend");if(n.length){var r=n[0];if("checkbox"===e.type||"radio"===e.type)return r;var o=r.getBoundingClientRect().top,i=e.getBoundingClientRect();if(i.height&&window.innerHeight)if(i.top+i.height-o<window.innerHeight/2)return r}}return document.querySelector("label[for='".concat(e.getAttribute("id"),"']"))||e.closest("label")}(t);return!!n&&(n.scrollIntoView(),t.focus({preventScroll:!0}),!0)}function a(e){c(e.target)&&e.preventDefault()}var u=function(){var e,t,n,o;e=document.querySelector("#toggle-menu"),t=document.querySelector("#close-menu"),n=document.querySelector("#header-navigation"),o=function(t){t.preventDefault(),r(e,"aria-expanded"),e.classList.toggle("is-active"),n.classList.toggle("js-show")},e&&t&&n&&[e,t].forEach((function(e){e.addEventListener("click",o)})),function(){var e=document.querySelector("#toggle-search"),t=document.querySelector("#close-search"),n=document.querySelector("#wrap-search"),o=document.querySelector("#content-header"),i=function(t){t.preventDefault(),r(e,"aria-expanded"),e.classList.toggle("is-active"),n.classList.toggle("js-show"),o.classList.toggle("js-show")};e&&t&&[e,t].forEach((function(e){e.addEventListener("click",i)}))}()};n(0);document.addEventListener("DOMContentLoaded",(function(){var e,t,n,r,c;document.querySelectorAll(".nhsuk-card--clickable").forEach((function(e){null!==e.querySelector("a")&&e.addEventListener("click",(function(){e.querySelector("a").click()}))})),e=document.querySelectorAll(".nhsuk-checkboxes--conditional .nhsuk-checkboxes__input"),t=function(e){o(e.target,"nhsuk-checkboxes__conditional--hidden")},e.forEach((function(e){e.addEventListener("change",t)})),i(),(n=document.querySelector(".nhsuk-error-summary"))&&(n.focus(),n.addEventListener("click",a)),u(),function(){var e=document.querySelectorAll(".nhsuk-radios--conditional .nhsuk-radios__input"),t=document.querySelectorAll(".nhsuk-radios--conditional .nhsuk-radios__conditional"),n=function(n){e.forEach((function(e){return e.setAttribute("aria-expanded","false")})),t.forEach((function(e){return e.classList.add("nhsuk-radios__conditional--hidden")})),o(n.target,"nhsuk-radios__conditional--hidden")};e.forEach((function(e){e.addEventListener("change",n)}))}(),r=document.querySelector("h1"),c=document.querySelector(".nhsuk-skip-link"),r&&c&&(c.addEventListener("click",(function(e){e.preventDefault(),r.setAttribute("tabIndex","-1"),r.focus()})),r.addEventListener("blur",(function(e){e.preventDefault(),r.removeAttribute("tabIndex")})))}));n(1)}]);