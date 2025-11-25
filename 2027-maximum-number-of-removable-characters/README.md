<h2><a href="https://leetcode.com/problems/maximum-number-of-removable-characters">Maximum Number of Removable Characters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given two strings <code>s</code> and <code>p</code> where <code>p</code> is a <strong>subsequence </strong>of <code>s</code>. You are also given a <strong>distinct 0-indexed </strong>integer array <code>removable</code> containing a subset of indices of <code>s</code> (<code>s</code> is also <strong>0-indexed</strong>).</p>

<p>You want to choose an integer <code>k</code> (<code>0 &lt;= k &lt;= removable.length</code>) such that, after removing <code>k</code> characters from <code>s</code> using the <strong>first</strong> <code>k</code> indices in <code>removable</code>, <code>p</code> is still a <strong>subsequence</strong> of <code>s</code>. More formally, you will mark the character at <code>s[removable[i]]</code> for each <code>0 &lt;= i &lt; k</code>, then remove all marked characters and check if <code>p</code> is still a subsequence.</p>

<p>Return <em>the <strong>maximum</strong> </em><code>k</code><em> you can choose such that </em><code>p</code><em> is still a <strong>subsequence</strong> of </em><code>s</code><em> after the removals</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcacb&quot;, p = &quot;ab&quot;, removable = [3,1,0]
<strong>Output:</strong> 2
<strong>Explanation</strong>: After removing the characters at indices 3 and 1, &quot;a<s><strong>b</strong></s>c<s><strong>a</strong></s>cb&quot; becomes &quot;accb&quot;.
&quot;ab&quot; is a subsequence of &quot;<strong><u>a</u></strong>cc<strong><u>b</u></strong>&quot;.
If we remove the characters at indices 3, 1, and 0, &quot;<s><strong>ab</strong></s>c<s><strong>a</strong></s>cb&quot; becomes &quot;ccb&quot;, and &quot;ab&quot; is no longer a subsequence.
Hence, the maximum k is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcbddddd&quot;, p = &quot;abcd&quot;, removable = [3,2,1,4,5,6]
<strong>Output:</strong> 1
<strong>Explanation</strong>: After removing the character at index 3, &quot;abc<s><strong>b</strong></s>ddddd&quot; becomes &quot;abcddddd&quot;.
&quot;abcd&quot; is a subsequence of &quot;<u><strong>abcd</strong></u>dddd&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcab&quot;, p = &quot;abc&quot;, removable = [0,1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation</strong>: If you remove the first index in the array removable, &quot;abc&quot; is no longer a subsequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= p.length &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= removable.length &lt; s.length</code></li>
	<li><code>0 &lt;= removable[i] &lt; s.length</code></li>
	<li><code>p</code> is a <strong>subsequence</strong> of <code>s</code>.</li>
	<li><code>s</code> and <code>p</code> both consist of lowercase English letters.</li>
	<li>The elements in <code>removable</code> are <strong>distinct</strong>.</li>
</ul>
