- [Принцип DRY](#org1e24104)
- [Декораторы](#orgf2b8832)
- [Декораторы в Django](#org22aaec5)
- [Function Based View](#orgbb8397b)
- [Class Based View](#orge257125)
- [Generic Based View](#orgced6e97)
- [Схема выбора](#orge42c4d3)
- [Дополнительная литература](#org765840a)



<a id="org1e24104"></a>

# Принцип DRY

-   **D:** on't  
    *не*
-   **R:** epeat  
    *повторяй*
-   **Y:** ourself  
    *-ся*


<a id="orgf2b8832"></a>

# Декораторы

```python
C = Callable[[Any], Any]
Callable[[C], C]
```


<a id="org22aaec5"></a>

# Декораторы в Django

<https://docs.djangoproject.com/en/4.2/topics/http/decorators/>  


<a id="orgbb8397b"></a>

# Function Based View


<a id="orge257125"></a>

# Class Based View


<a id="orgced6e97"></a>

# Generic Based View


<a id="orge42c4d3"></a>

# Схема выбора

![img](flowchart.png)  


<a id="org765840a"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[Python Design Patterns](https://python-patterns.guide/)</span></span>
-   <span class="underline"><span class="underline">[Blog](https://testdriven.io/blog/django-class-based-vs-function-based-views/)</span></span>
-   <span class="underline"><span class="underline">[Mixins](https://django.fun/ru/docs/django/4.0/topics/class-based-views/mixins/)</span></span>
