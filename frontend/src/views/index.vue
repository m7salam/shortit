<script>
import {
  ArrowUpIcon,
  ArrowRightIcon,
  ArrowRightCircleIcon,
  HelpCircleIcon
} from "vue-feather-icons";
import Navbar from "@/components/navbar";
import axios from "axios";

/**
 * Index homepage component
 */
export default {
  data() {
    return {
      urlInput: "",
      short_url: "",
      shortcode: "",
      count: 0,
      count_exist: false
    };
  },
  components: {
    Navbar,
    ArrowUpIcon,
    ArrowRightIcon,
    ArrowRightCircleIcon,
    HelpCircleIcon
  },
  methods: {
    submitForm: function() {
      axios
        .post("/shortit/", { url: `${this.urlInput}` })
        .then(res => {
          this.short_url = res.data.short_url;
          this.urlInput = this.short_url;
          this.shortcode = res.data.shortcode;
          this.count = 0;
          this.get_url_count();
        })
        .catch(error => {
          console.log(error);
        });
    },
    get_url_count: function() {
      axios
        .get(`/analytics/count/?q=${this.shortcode}`)
        .then(res => {
          this.count = res.data.count;
          this.count_exist = true;
        })
        .catch(err => {
          console.error(err);
        });
    }
  }
};
</script>

<template>
  <div>
    <Navbar :nav-light="true" />
    <!-- Start Home -->
    <section
      class="bg-home d-flex align-items-center bg-animation-left task-management-home"
      style="height: auto"
      id="home"
    >
      <div class="container position-relative" style="z-index: 1">
        <div class="row justify-content-center">
          <div class="col-lg-12 text-center mt-0 mt-md-5 pt-0 pt-md-5">
            <div class="title-heading margin-top-100">
              <h1 class="heading text-white title-dark mb-3">
                Welcome to short.it
              </h1>
              <p class="para-desc mx-auto text-white-50">
                where you can make urls shorter
              </p>
              <div class="text-center subcribe-form mt-4 pt-2">
                <p v-show="count_exist" class="para-desc mx-auto text-white-50">
                  count: {{ count }}
                </p>
                <form v-on:submit.prevent>
                  <div class="form-group mb-0">
                    <input
                      v-model="urlInput"
                      type="url"
                      id="url"
                      name="url"
                      class="border rounded-pill"
                      required
                      placeholder="insert a valid url"
                    />
                    <button
                      @click="submitForm"
                      type="submit"
                      class="btn btn-pills btn-primary"
                    >
                      shorten
                    </button>
                  </div>
                </form>
              </div>
            </div>

            <div class="row justify-content-center">
              <div class="col-lg-10 text-center">
                <div class="home-dashboard">
                  <img src="images/task/laptop.png" alt="" class="img-fluid" />
                </div>
              </div>
            </div>
          </div>
          <!--end col-->
        </div>
        <!--end row-->
      </div>
      <!--end container-->
    </section>
    <!--end section-->
    <!-- End Home -->

    <!-- <Switcher /> -->
    <!-- Back to top -->
    <a
      href="javascript: void(0);"
      class="btn btn-icon btn-soft-primary back-to-top"
      id="back-to-top"
      v-scroll-to="'#topnav'"
    >
      <arrow-up-icon class="icons"></arrow-up-icon>
    </a>
    <!-- Back to top -->
  </div>
</template>
