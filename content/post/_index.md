---
title: "Recent posts"
layout: recents
description: Posts with snippets.
---

<!-- Main Content -->
<div class="container">
    <div class="row">
    <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
    {{ print "hello" }}
        {{ range .Paginator.Pages }}
            {{ .Render "list" }}
        {{ end }}
        {{ partial "pagination.html" . }}
    </div>
    </div>
</div>
