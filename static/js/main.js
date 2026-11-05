const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#primary-navigation");

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isExpanded = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!isExpanded));
    navigation.classList.toggle("is-open", !isExpanded);
  });

  navigation.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement && window.matchMedia("(max-width: 600px)").matches) {
      menuButton.setAttribute("aria-expanded", "false");
      navigation.classList.remove("is-open");
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      menuButton.setAttribute("aria-expanded", "false");
      navigation.classList.remove("is-open");
      menuButton.focus();
    }
  });
}

const revealElements = document.querySelectorAll(
  ".section-heading, .about-copy, .skill-group, .project-card, .services-intro, .service-card, .contact-panel",
);
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if ("IntersectionObserver" in window && !prefersReducedMotion) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealElements.forEach((element) => {
    element.classList.add("reveal");
    revealObserver.observe(element);
  });

  const counters = document.querySelectorAll("[data-count]");
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      const counter = entry.target;
      const total = Number(counter.dataset.count);
      const start = performance.now();
      const duration = 850;

      const updateCounter = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        counter.textContent = String(Math.round(total * progress));
        if (progress < 1) requestAnimationFrame(updateCounter);
      };

      requestAnimationFrame(updateCounter);
      observer.unobserve(counter);
    });
  }, { threshold: 0.7 });

  counters.forEach((counter) => counterObserver.observe(counter));
}

const sectionLinks = document.querySelectorAll(".site-nav a[data-section]");
const sections = Array.from(sectionLinks)
  .map((link) => document.getElementById(link.dataset.section))
  .filter((section) => section instanceof HTMLElement)
  .sort((first, second) => first.offsetTop - second.offsetTop);

if (sections.length > 0) {
  const updateActiveSection = () => {
    const activationLine = window.innerHeight * 0.38;
    const passedSections = sections.filter(
      (section) => section.getBoundingClientRect().top <= activationLine,
    );
    const activeSection = passedSections[passedSections.length - 1] || sections[0];

    sectionLinks.forEach((link) => {
      if (link.dataset.section === activeSection.id) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  let activeSectionFrame = 0;
  window.addEventListener("scroll", () => {
    if (activeSectionFrame) return;
    activeSectionFrame = window.requestAnimationFrame(() => {
      updateActiveSection();
      activeSectionFrame = 0;
    });
  }, { passive: true });
  window.addEventListener("resize", updateActiveSection);
  updateActiveSection();
}

const parallaxProfile = document.querySelector("[data-parallax]");
if (parallaxProfile instanceof HTMLElement && !prefersReducedMotion) {
  let parallaxFrame = 0;
  window.addEventListener("scroll", () => {
    if (parallaxFrame) return;
    parallaxFrame = window.requestAnimationFrame(() => {
      const offset = Math.min(window.scrollY * 0.045, 22);
      parallaxProfile.style.setProperty("--profile-parallax", `${offset}px`);
      parallaxFrame = 0;
    });
  }, { passive: true });
}
