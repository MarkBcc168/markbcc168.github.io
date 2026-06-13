function expand_all(shouldExpand){
    let detailsElements = document.querySelectorAll("details");

    for(let item of detailsElements){
      if (item.hasAttribute("open") !== shouldExpand) {
          item.querySelector("summary").click();
      }
    } 
};

function get_hash_link_tag(text){
    return text.trim().toLowerCase()
                .replaceAll(" ", "_")
                .replaceAll("\(", "")
                .replaceAll("\)","")
                .replaceAll("/","-")
                .replaceAll("\\", "")
                .replaceAll("<","")
                .replaceAll(">","");
}

class Accordion {
  constructor(el) {
    // Store the <details> element
    this.el = el;
    // Store the <summary> element
    this.summary = el.querySelector('summary');
    for(let elem of this.summary.querySelectorAll('a')){
      elem.addEventListener('click', (e) => e.stopPropagation());
    }
    // Store the <div class="details-content"> element
    this.content = el.querySelector('.details-content');

    // Store the animation object (so we can cancel it if needed)
    this.animation = null;
    // Store if the element is closing
    this.isClosing = false;
    // Store if the element is expanding
    this.isExpanding = false;
    // Detect user clicks on the summary element
    this.summary.addEventListener('click', (e) => this.onClick(e));
  }

  onClick(e) {
    e.preventDefault();
    this.el.style.overflow = 'hidden';
    if (this.isClosing || !this.el.open) {
      this.open();
    } else if (this.isExpanding || this.el.open) {
      this.shrink();
    }
  }

  shrink() {
    // Set the element as "being closed"
    this.isClosing = true;
    
    // Store the current height of the element
    const startHeight = `${this.el.offsetHeight}px`;
    // Calculate the height of the summary
    const endHeight = `${this.summary.offsetHeight}px`;
    
    // If there is already an animation running
    if (this.animation) {
      // Cancel the current animation
      this.animation.cancel();
    }
    
    // Start a WAAPI animation
    this.animation = this.el.animate({
      // Set the keyframes from the startHeight to endHeight
      height: [startHeight, endHeight]
    }, {
      duration: this.content.offsetHeight * 2 / 3,
      easing: 'ease-out'
    });
    
    // When the animation is complete, call onAnimationFinish()
    this.animation.onfinish = () => this.onAnimationFinish(false);
    // If the animation is cancelled, isClosing variable is set to false
    this.animation.oncancel = () => this.isClosing = false;
  }

  open() {
    // Apply a fixed height on the element
    this.el.style.height = `${this.el.offsetHeight}px`;
    // Force the [open] attribute on the details element
    this.el.open = true;
    // Wait for the next frame to call the expand function
    window.requestAnimationFrame(() => this.expand());
  }

  expand() {
    // Set the element as "being expanding"
    this.isExpanding = true;
    // Get the current fixed height of the element
    const startHeight = `${this.el.offsetHeight}px`;
    // Calculate the open height of the element (summary height + content height)
    const endHeight = `${this.summary.offsetHeight + this.content.offsetHeight}px`;
    
    // If there is already an animation running
    if (this.animation) {
      // Cancel the current animation
      this.animation.cancel();
    }
    
    // Start a WAAPI animation
    this.animation = this.el.animate({
      // Set the keyframes from the startHeight to endHeight
      height: [startHeight, endHeight]
    }, {
      duration: this.content.offsetHeight * 2 / 3,
      easing: 'ease-out'
    });
    // When the animation is complete, call onAnimationFinish()
    this.animation.onfinish = () => this.onAnimationFinish(true);
    // If the animation is cancelled, isExpanding variable is set to false
    this.animation.oncancel = () => this.isExpanding = false;
  }

  onAnimationFinish(open) {
    // Set the open attribute based on the parameter
    this.el.open = open;
    // Clear the stored animation
    this.animation = null;
    // Reset isClosing & isExpanding
    this.isClosing = false;
    this.isExpanding = false;
    // Remove the overflow hidden and the fixed height
    this.el.style.height = this.el.style.overflow = '';
  }
}



document.addEventListener('DOMContentLoaded', () => {
    //create hash link
    let headerElements = document.querySelectorAll("h1, h2, h3, h4, h5, h6, div.paper-title");
    for(let elem of headerElements){
        if(elem.id == "no-hash"){
            continue;
        }
        text = elem.innerHTML;
        tag = get_hash_link_tag(text);
        elem.innerHTML = `<a id="${tag}"></a>${text}<a href="#${tag}" class="hash-link"><i class="fa fa-link"></i></a>`;
    }

    //setup abstract
    let abstractElements = document.querySelectorAll("p#abstract");
    for(let elem of abstractElements){
        text = elem.innerHTML;
        elem.innerHTML = "<b>Abstract</b><br>" + text;
    }
    //setup animation
    document.querySelectorAll('details').forEach((el) => {
        new Accordion(el);
    });
});



